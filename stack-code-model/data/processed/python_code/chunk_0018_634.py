class zcl_aps_task_starter_batch definition
  public
  inheriting from zcl_aps_task_starter
  final
  create private
  global friends zcl_aps_task_starter_factory.

  public section.
    methods:
      zif_aps_task_starter~start redefinition.
    METHODS: zif_aps_task_starter~retry REDEFINITION,
             zif_aps_task_starter~resume REDEFINITION.

  protected section.

  private section.
    types:
      jobReference        type ref to zif_aps_batch_job,
      jobChainType        type standard table of jobReference
                               with default key,
      jobChainListType    type standard table of jobChainType
                               with default key,
      jobNameRange        type range of btcjob,
      jobUniqueIdRange    type range of btcjobcnt.

    methods:
      createTaskChains
        importing
          i_packages      type ref to zaps_packages
        returning
          value(result)   type zaps_task_chains
        raising
          zcx_aps_task_creation_error,

      createJobChains
        importing
          i_taskChains    type zaps_task_chains
        returning
          value(result)   type jobChainListType
        raising
          zcx_aps_job_creation_error,

      createJobChain
        importing
          i_taskChain           type ref to zaps_task_chain
          value(i_chainNumber)  type sytabix
        returning
          value(result)         type jobChainType
        raising
          zcx_aps_job_creation_error,

      doWaitUntilFinished
        importing
          i_jobChains           type jobChainListType,

      hasAbortedJobs
        importing
          i_jobChains           type jobChainListType
        returning
          value(result)         type abap_bool,

      detJobListFromJobChains
        importing
          i_jobChains      type jobchainlisttype
        returning
          value(result)    type zaps_batch_job_list,

      startTasks
        importing
          i_taskchains    type zaps_task_chains
        returning
          value(r_result) type zaps_parameter_set_list
        raising
          zcx_aps_job_creation_error
          zcx_aps_jobs_aborted,

      splitTaskListToTaskChains
        importing
          i_tasks             type zaps_task_chain
        returning
          value(result) type zaps_task_chains.
endclass.



class zcl_aps_task_starter_batch implementation.
  method zif_aps_task_starter~start.
    if not i_packages is bound
    or i_packages->* is initial.
      return.
    endif.

    data(taskChains) = createTaskChains( i_packages ).

    result = startTasks( taskchains ).
  endmethod.


  method zif_aps_task_starter~resume.
    try.
      data(tasks) = zcl_aps_task_storage_factory=>provide( )->loadTasksForResume( settings->getRunId( ) ).
    catch zcx_aps_task_storage
          zcx_aps_task_serialization
    into data(storageError).
      message storageError
      type 'I'
      display like 'E'.

      return.
    endtry.

    result = startTasks( splitTaskListToTaskChains( tasks ) ).
  endmethod.


  method zif_aps_task_starter~retry.
    try.
      data(tasks) = zcl_aps_task_storage_factory=>provide( )->loadTasksForRetry( settings->getRunId( ) ).
    catch zcx_aps_task_storage
          zcx_aps_task_serialization
    into data(storageError).
      message storageError
      type 'I'
      display like 'E'.

      return.
    endtry.

    result = startTasks( splitTaskListToTaskChains( tasks ) ).
  endmethod.


  method splitTaskListToTaskChains.

    data(numberOfNeededChains) = nmin(
                                   val1 = lines( i_tasks )
                                   val2 = settings->getmaxparalleltasks( )
                                 ).

    do numberOfNeededChains times.
      append initial line
      to result.
    enddo.

    loop at i_tasks
    into data(task).
      " Modulo only works with table indices starting at 0. ABAP instead starts counting at 1.
      " This -1/+1 ensures correct indices for tasks n*numberofNeededTasks (last Chain)
      data(chainNumber) = ( ( sy-tabix - 1 ) mod numberOfNeededChains ) + 1.

      " ABAP doesn't like nested tables inside append command ...
      data(chainReference) = ref #( result[ chainNumber ] ).

      append task
      to chainReference->*.
    endloop.

  endmethod.


  method startTasks.

    data(jobChains) = createJobChains( i_taskchains ).

    " When all job chains have been created successfully, raise the event to start them
    cl_batch_event=>raise(
      exporting
        i_eventid                      = zif_aps_batch_job=>c_jobStartEvent
        i_eventparm                    = conv btcevtparm( settings->getAppId( ) )
      exceptions
        excpt_raise_failed             = 1
        excpt_server_accepts_no_events = 2
        excpt_raise_forbidden          = 3
        excpt_unknown_event            = 4
        excpt_no_authority             = 5
        others                         = 6
    ).

    if sy-subrc <> 0.
      data(detailledError) = new zcx_aps_task_job_event_raise(
                               i_eventname = zif_aps_batch_job=>c_jobStartEvent
                               i_errorcode = sy-subrc
                             ).

      raise exception
        type zcx_aps_job_creation_error
        exporting
          i_previous = detailledError.
    endif.

    settings->setStatusRunning( ).

    doWaitUntilFinished( jobChains ).

    " loading the tasks does delete them from the temporary table
    " that's why it is always done.
    try.
        data(tasklist) = zcl_aps_task_storage_factory=>provide( )->loadalltasks( settings->getRunId( ) ).
      catch zcx_aps_task_storage
            zcx_aps_task_serialization
      into data(storageErrorLoad).
        message storageErrorLoad
        type 'I'
        display like 'E'.

        taskList = value zaps_task_chain( ).
    endtry.

    " check job status for aborted ones
    if hasAbortedJobs( jobChains ) = abap_true.
      settings->setStatusAborted( ).

      " no sense in collecting results
      raise exception
        type zcx_aps_jobs_aborted.
    endif.

    " receiving the results is only useful if we waited for completion
    if settings->shouldWaitUntilFinished( ) = abap_true.
      loop at taskList
      into data(task).
        insert lines of task->getPackage( )-selections
        into table r_result.
      endloop.
    endif.

  endmethod.


  method createTaskChains.
    data(numberOfNeededChains) = nmin(
                                   val1 = lines( i_packages->* )
                                   val2 = settings->getmaxparalleltasks( )
                                 ).

    do numberOfNeededChains times.
      append initial line
      to result.
    enddo.

    loop at i_packages->*
    reference into data(package).
      " Modulo only works with table indices starting at 0. ABAP instead starts counting at 1.
      " This -1/+1 ensures correct indices for tasks n*numberofNeededTasks (last Chain)
      data(chainNumber) = ( ( sy-tabix - 1 ) mod numberOfNeededChains ) + 1.

      " ABAP doesn't like nested tables inside append command ...
      data(chainReference) = ref #( result[ chainNumber ] ).

      append createTask( package )
      to chainReference->*.
    endloop.
  endmethod.

  method createJobChain.
    data:
      previousJob     type ref to zif_aps_batch_job.

    try.
      loop at i_taskChain->*
      into data(task).
        data(taskNumberInChain) = sy-tabix.
        data(isFirstTaskOfChain) = switch abap_bool(
                                     sy-tabix
                                     when 1 then abap_true
                                     else abap_false
                                   ).

        zcl_aps_task_storage_factory=>provide( )->storetask( task ).

        data(job) = zcl_aps_batch_job_factory=>provide(
                      i_task                = task
                      i_settings            = settings
                      i_chainnumber         = i_chainNumber
                      i_tasknumberinchain   = taskNumberInChain
                    ).

        job->create( ).

        job->addstep( ).

        " The first job of each chain is started by an event
        " If it would start directly it could have been finished before the successor is even released
        if isFirstTaskOfChain = abap_true.
          job->planAsEventTriggered( ).
        else.
          job->planAsSuccessor( previousJob ).
        endif.

        insert job
        into table result.

        previousJob = job.
      endloop.
    catch zcx_aps_task_job_creation
          zcx_aps_task_job_submit
          zcx_aps_task_job_release
          zcx_aps_task_storage
          zcx_aps_task_serialization
    into data(detailledJobError).
      raise exception
      type zcx_aps_job_creation_error
      exporting
        i_previous  = detailledJobError.
    endtry.
  endmethod.

  method createJobChains.
    loop at i_taskChains
    reference into data(taskChain).
      insert createJobChain(
               i_taskchain   = taskChain
               i_chainnumber = sy-tabix
             )
      into table result.
    endloop.
  endmethod.


  method doWaitUntilFinished.
    if settings->shouldwaituntilfinished( ) = abap_false.
      return.
    endif.

    data(joblist) = detJobListFromJobChains( i_jobchains ).

    while zcl_aps_batch_job=>arealljobsfinished( jobList ) = abap_false.
      wait up to 10 seconds.
    endwhile.
  endmethod.

  method detJobListFromJobChains.
    " The jobs of one chain start in a sequence but do not care about
    " the result of the predecessor (finished/aborted). So all jobs
    " must have one of these status in order to be finished.
    result  = value zaps_batch_job_list(
                  for jobChain in i_jobChains
                    for job in jobChain
                    (
                      jobname      = job->getjobname( )
                      jobuniqueid  = job->getjobuniqueid( )
                    )
                ).
  endmethod.


  method hasAbortedJobs.
    loop at i_jobChains
    reference into data(jobChain).
      loop at jobChain->*
      into data(job).
        if job->isAborted( ) = abap_true.
          result = abap_true.
          return.
        endif.
      endloop.
    endloop.
  endmethod.

endclass.