import libc;
import llvm;
import code;
import dict;
import list;
import types;
import errors;
import ast;
import generator_;
import generator_util;
import resolver;
import builder;

# Generate the `type` of each declaration "item".
# -----------------------------------------------------------------------------
let generate(mut g: generator_.Generator) ->
{
    # Iterate over the "items" dictionary.
    let mut i: dict.Iterator = g.items.iter();
    let mut key: str;
    let mut ptr: *int8;
    let mut val: *code.Handle;
    while not i.empty() {
        # Grab the next "item"
        let tup = i.next();
        (key, ptr) = tup;
        val = ptr as *code.Handle;

        # Does this item need its `type` resolved?
        if     val._tag == code.TAG_STATIC_SLOT
            or val._tag == code.TAG_FUNCTION
            or val._tag == code.TAG_STRUCT
            or val._tag == code.TAG_EXTERN_FUNC
            or val._tag == code.TAG_EXTERN_STATIC
            or val._tag == code.TAG_ATTACHED_FUNCTION
        {
            generate_handle(g, key, val);
        };
    }
}

# Generate the `type` for the passed code handle.
# -----------------------------------------------------------------------------
let generate_handle(mut g: generator_.Generator, qname: str,
                    handle: *code.Handle)
   : *code.Handle ->
{
    # Resolve the type based on the tag of handle.
    if handle._tag == code.TAG_STATIC_SLOT
    {
        generate_static_slot(g, qname, handle._object as *code.StaticSlot);
    }
    else if handle._tag == code.TAG_FUNCTION
    {
        generate_function(g, qname, handle._object as *code.Function);
    }
    else if handle._tag == code.TAG_ATTACHED_FUNCTION
    {
        generate_attached_function(g, qname,
                                   handle._object as *code.AttachedFunction);
    }
    else if handle._tag == code.TAG_STRUCT
    {
        generate_struct(g, qname, handle._object as *code.Struct);
    }
    # else if handle._tag == code.TAG_STRUCT_MEM
    # {
    #     generate_struct_mem(g, handle._object as *code.StructMem);
    # }
    else if handle._tag == code.TAG_EXTERN_FUNC
    {
        generate_extern_function(g, qname, handle._object as *code.ExternFunction);
    }
    else if handle._tag == code.TAG_EXTERN_STATIC
    {
        generate_extern_static(g, qname, handle._object as *code.ExternStatic);
    }
    else
    {
        errors.begin_error();
        errors.libc.fprintf(errors.libc.stderr, "not implemented: generator_type.generate_handle(%d)", handle._tag);
        errors.end();
        code.make_nil();
    };
}

# Generate the type for the `static slot`.
# -----------------------------------------------------------------------------
let generate_static_slot(mut g: generator_.Generator,
                         qname: str, x: *mut code.StaticSlot)
   : *code.Handle ->
{
    # Return our type if it is resolved.
    if not code.isnil(x.type_) { return x.type_; };

    # Return nil if we have been poisioned from a previous failure.
    if code.ispoison(x.type_) { return code.make_nil(); };

    # If we have a type node ...
    let mut han: *code.Handle;
    if not ast.isnull(x.context.type_)
    {
        # ... get and resolve the type node.
        han = resolver.resolve_in(
            &g, &x.context.type_, &x.namespace,
            code.make_nil_scope(),
            code.make_nil());
    }
    else if not ast.isnull(x.context.initializer)
    {
        # ... else; resolve the initializer.
        han = resolver.resolve_in(
            &g, &x.context.initializer, &x.namespace,
            code.make_nil_scope(),
            code.make_nil());
    }
    else
    {
        # Bail; static slot declarations require either an initializer
        # or a type.
        errors.begin_error();
        errors.libc.fprintf(errors.libc.stderr, "static slots require either an an initializer or a type");
        errors.end();

        return code.make_nil();
    };

    # Store and return our type handle (or poision if we failed).
    x.type_ = han;
}

# Generate the return type for a `function-like`.
# -----------------------------------------------------------------------------
let _generate_return_type(mut g: generator_.Generator,
                          x: *ast.Node,
                          namespace: *list.List,
                          scope: *code.Scope): *code.Handle ->
{

    # Resolve the return type.
    let mut ret_han: *code.Handle = code.make_nil();
    if ast.isnull(*x)
    {
        # No return type specified.
        # TODO: In the future this should resolve the type
        #   of the function body.
        # Use a void return type for now.
        ret_han = code.make_void_type(llvm.LLVMVoidType());
    }
    else
    {
        # Get and resolve the return type.
        ret_han = resolver.resolve_in(
            &g, x, namespace, scope, code.make_nil());
        if not code.is_type(ret_han) {
            ret_han = code.type_of(ret_han);
        };

        if code.isnil(ret_han) { return code.make_nil(); };
    };

    # Return the ret handle.
    return ret_han;
}

# Generate the type for the `function`.
# -----------------------------------------------------------------------------
let generate_function(mut g: generator_.Generator,
                      qname: str, x: *code.Function)
   : *code.Handle ->
{
    # Return our type if it is resolved.
    if not code.isnil(x.type_) { return x.type_; };

    # Return nil if we have been poisioned from a previous failure.
    if code.ispoison(x.type_) { return code.make_nil(); };

    # Resolve the return type.
    let ret_han: *code.Handle = _generate_return_type(
        g,
        &x.context.return_type,
        &x.namespace,
        &x.scope);
    if code.isnil(ret_han) {
        x.type_ = code.make_poison();
        return code.make_poison();
    };
    let ret_typ: *code.Type = ret_han._object as *code.Type;
    let mut ret_typ_han: *llvm.LLVMOpaqueType;
    ret_typ_han = generator_util.alter_type_handle(ret_han);

    # Resolve the type for each parameter.
    let mut params: list.List = list.List.new(types.PTR);
    let mut param_type_handles: list.List = list.List.new(types.PTR);
    let mut i: int = 0;
    while i as uint < x.context.params.size()
    {
        let pnode: ast.Node = x.context.params.get(i);
        i = i + 1;
        let p: *ast.FuncParam = pnode.unwrap() as *ast.FuncParam;
        if not _generate_func_param(
            g, p, &x.namespace, &x.scope, params, param_type_handles, true)
        {
             # Failed to resolve type; mark us as poisioned.
             x.type_ = code.make_poison();
             return code.make_poison();
        };
    }

    # Build the LLVM type handle.
    let mut val: *llvm.LLVMOpaqueType;
    val = llvm.LLVMFunctionType(
        ret_typ_han,
        param_type_handles.elements as **llvm.LLVMOpaqueType,
        param_type_handles.size as uint32,
        0);

    # Create and store our type.
    let mut han: *code.Handle;
    han = code.make_function_type(
        qname, x.namespace, x.name.data() as str, val, ret_han, params);
    x.type_ = han;

    # Dispose of dynamic memory.
    param_type_handles.dispose();

    # Return the type handle.
    han;
}

# Generate the type for the `attached function`.
# -----------------------------------------------------------------------------
let generate_attached_function(mut g: generator_.Generator,
                               qname: str,
                               x: *code.AttachedFunction)
   : *code.Handle ->
{
    # Return our type if it is resolved.
    if not code.isnil(x.type_) { return x.type_; };

    # Return nil if we have been poisioned from a previous failure.
    if code.ispoison(x.type_) { return code.make_nil(); };

    # Resolve the return type.
    let ret_han: *code.Handle = _generate_return_type(
        g,
        &x.context.return_type,
        &x.namespace,
        &x.scope);
    if code.isnil(ret_han) {
        x.type_ = code.make_poison();
        return code.make_poison();
    };
    let ret_typ: *code.Type = ret_han._object as *code.Type;
    let mut ret_typ_han: *llvm.LLVMOpaqueType;
    ret_typ_han = generator_util.alter_type_handle(ret_han);

    let mut params: list.List = list.List.new(types.PTR);
    let mut param_type_handles: list.List = list.List.new(types.PTR);
    let mut i: int = 0;

    # Check for "self"
    if x.context.instance {
        # Push a parameter for "self"
        let self_type_handle: *code.Handle = _generate_func_param_wrap(
            x.attached_type,
            generator_util.alter_type_handle(x.attached_type));
        let self_type: *code.Type = self_type_handle._object as *code.Type;
        param_type_handles.push_ptr(self_type.handle as *int8);
        let param: *code.Handle = code.make_parameter(
            "self",
            self_type_handle,
            code.make_nil(), false);
        params.push_ptr(param as *int8);
    };

    # Resolve the type for each parameter.
    while i as uint < x.context.params.size()
    {
        let pnode: ast.Node = x.context.params.get(i);
        i = i + 1;
        let p: *ast.FuncParam = pnode.unwrap() as *ast.FuncParam;
        if not _generate_func_param(
            g, p, &x.namespace, &x.scope, params, param_type_handles, true)
        {
             # Failed to resolve type; mark us as poisioned.
             x.type_ = code.make_poison();
             return code.make_poison();
        };
    }

    # Build the LLVM type handle.
    let mut val: *llvm.LLVMOpaqueType;
    val = llvm.LLVMFunctionType(
        ret_typ_han,
        param_type_handles.elements as **llvm.LLVMOpaqueType,
        param_type_handles.size as uint32,
        0);

    # Create and store our type.
    let mut han: *code.Handle;
    han = code.make_function_type(
        "", x.namespace, x.name.data() as str, val, ret_han, params);
    x.type_ = han;

    # Dispose of dynamic memory.
    param_type_handles.dispose();

    # Return the type handle.
    han;
}

# Generate the type for the `struct`.
# -----------------------------------------------------------------------------
let generate_struct(mut g: generator_.Generator, qname: str, x: *code.Struct)
   : *code.Handle ->
{
    # Return our type if it is resolved.
    if not code.isnil(x.type_) { return x.type_; };

    # Return nil if we have been poisioned from a previous failure.
    if code.ispoison(x.type_) { return code.make_nil(); };

    # Build the `opaque` type handle.
    let mut val: *llvm.LLVMOpaqueType;
    val = llvm.LLVMStructCreateNamed(llvm.LLVMGetGlobalContext(), qname);

    # Create and store our type.
    let mut han: *code.Handle;
    han = code.make_struct_type(qname, x.context, x.namespace, val);
    x.type_ = han;

    # Return the type handle.
    han;
}

# Generate the type for a member of the `struct`.
# -----------------------------------------------------------------------------
let generate_struct_member(mut g: generator_.Generator,
                           x: *code.StructType, name: str)
   : *code.Handle ->
{
    # Has this member been placed in the structure yet?
    if x.member_map.contains(name) {
        # Is this a poision from a previous failure?
        let han: *code.Handle = x.member_map.get(name) as *code.Handle;
        if code.ispoison(han) { return code.make_nil(); };

        if not code.isnil(han) {
            # Return the resolved type.
            let mem: *code.Member = han._object as *code.Member;
            return mem.type_;
        };
    };

    # Does this member exist on the structure?
    # FIXME: The AST should generate a dictionary for me to use here.
    let mut i: int = 0;
    let mut mnode: ast.Node;
    let mut m: *ast.StructMem = 0 as *ast.StructMem;
    while i as uint < x.context.nodes.size() {
        mnode = x.context.nodes.get(i);
        let mtmp: *ast.StructMem = mnode.unwrap() as *ast.StructMem;
        i = i + 1;

        # Check for the name.
        let id: *ast.Ident = mtmp.id.unwrap() as *ast.Ident;
        if id.name.eq_str(name) {
            # Found one; get out.
            m = mtmp;
            break;
        };
    }

    # Did we manage to find a member?
    if m == 0 as *ast.StructMem {
        # Nope; report the error and bail.
        x.member_map.set_ptr(name, code.make_poison() as *int8);
        errors.begin_error();
        errors.libc.fprintf(errors.libc.stderr,
                       "type '%s' has no member '%s'",
                       x.name.data(), name);
        errors.end();
        return code.make_nil();
    };

    # Resolve the type of the structure member.
    let type_handle: *code.Handle = resolver.resolve_in_t(
        &g, &m.type_, &x.namespace, code.make_nil());
    if code.isnil(type_handle) {
        x.member_map.set_ptr(name, code.make_poison() as *int8);
        return code.make_nil();
    };

    # Emplace the solid type.
    x.member_map.set_ptr(name, code.make_member(
        name,
        type_handle,
        (i as uint - 1) as uint,
        code.make_nil()) as *int8);

    # Return the type.
    type_handle;
}

# Generate the type for the external `static`.
# -----------------------------------------------------------------------------
let generate_extern_static(mut g: generator_.Generator,
                           qname: str, x: *code.ExternStatic)
   : *code.Handle ->
{
    # Return our type if it is resolved.
    if not code.isnil(x.type_) { return x.type_; };

    # Return nil if we have been poisioned from a previous failure.
    if code.ispoison(x.type_) { return code.make_nil(); };

    # Get and resolve the type node.
    let mut han: *code.Handle;
    han = resolver.resolve_in(
        &g, &x.context.type_, &x.namespace,
        code.make_nil_scope(),
        code.make_nil());

    # Store and return our type handle (or poision if we failed).
    x.type_ = han;
}

# Generate the type for the external `function`.
# -----------------------------------------------------------------------------
let generate_extern_function(mut g: generator_.Generator,
                             qname: str, x: *code.ExternFunction)
   : *code.Handle ->
{
    # Return our type if it is resolved.
    if not code.isnil(x.type_) { return x.type_; };

    # Return nil if we have been poisioned from a previous failure.
    if code.ispoison(x.type_) { return code.make_nil(); };

    # Resolve the return type.

    # Resolve the return type.
    let ret_han: *code.Handle = _generate_return_type(
        g,
        &x.context.return_type,
        &x.namespace,
        code.make_nil_scope());
    if code.isnil(ret_han) {
        x.type_ = code.make_poison();
        return code.make_poison();
    };
    let ret_typ: *code.Type = ret_han._object as *code.Type;
    let mut ret_typ_han: *llvm.LLVMOpaqueType;
    ret_typ_han = generator_util.alter_type_handle(ret_han);

    # Resolve the type for each parameter.
    let mut params: list.List = list.List.new(types.PTR);
    let mut param_type_handles: list.List = list.List.new(types.PTR);
    let mut i: int = 0;
    let mut variadic: bool = false;
    while i as uint < x.context.params.size()
    {
        let pnode: ast.Node = x.context.params.get(i);
        i = i + 1;
        let p: *ast.FuncParam = pnode.unwrap() as *ast.FuncParam;

        if p.variadic {
            variadic = true;
        };

        if not _generate_func_param(
            g, p, &x.namespace, code.make_nil_scope(),
            params, param_type_handles, false)
        {
             # Failed to resolve type; mark us as poisioned.
             x.type_ = code.make_poison();
             return code.make_poison();
        };

        if variadic {
            # This is now a "variadic" function and it is closed.
            break;
        };
    }

    # Build the LLVM type handle.
    let mut val: *llvm.LLVMOpaqueType;
    val = llvm.LLVMFunctionType(
        ret_typ_han,
        param_type_handles.elements as **llvm.LLVMOpaqueType,
        param_type_handles.size as uint32,
        1 if variadic else 0);

    # Create and store our type.
    let mut han: *code.Handle;
    han = code.make_function_type(
        qname, x.namespace, x.name.data() as str, val, ret_han, params);
    x.type_ = han;

    # Dispose of dynamic memory.
    param_type_handles.dispose();

    # Return the type handle.
    han;
}

# Helper: Wrap a parameter tpye
let _generate_func_param_wrap(handle: *code.Handle, value: *llvm.LLVMOpaqueType): *code.Handle ->
{
    # Decide if we need to "wrap" the type as a reference type.
    let mut type_: *code.Handle = handle;
    let han: *code.Type = type_._object as *code.Type;
    han.handle = value;
    if type_._tag == code.TAG_STRUCT_TYPE
        or type_._tag == code.TAG_ARRAY_TYPE
    {
        # Yes, wrap the type as a reference.
        let val: *llvm.LLVMOpaqueType = llvm.LLVMPointerType(
            value, 0);
        type_ = code.make_reference_type(type_, false, val);
    };
    return type_;
}

# Helper: Generate the type for a parameter
# -----------------------------------------------------------------------------
let _generate_func_param(
    mut g: generator_.Generator,
    x: *ast.FuncParam,
    namespace: *mut list.List,
    scope: *mut code.Scope,
    mut types: list.List,
    mut handles: list.List,
    arrow_cc: bool): bool ->
{
    let mut ptype_handle: *code.Handle = code.make_nil();
    if not x.variadic {
        # Resolve the type.
        ptype_handle = resolver.resolve_in(
            &g, &x.type_, namespace, scope, code.make_nil());
        if code.isnil(ptype_handle) { return false; };
        if not code.is_type(ptype_handle) {
            ptype_handle = code.type_of(ptype_handle);
        };

        ptype_handle = _generate_func_param_wrap(
            ptype_handle, generator_util.alter_type_handle(ptype_handle));
        let type_: *code.Type = ptype_handle._object as *code.Type;
        let type_handle: *llvm.LLVMOpaqueType = type_.handle;

        # Emplace the type handle.
        handles.push_ptr(type_handle as *int8);
    };

    if not ast.isnull(x.id)
    {
        # Emplace a solid, named parameter.
        let param_id: *ast.Ident = x.id.unwrap() as *ast.Ident;
        types.push_ptr(code.make_parameter(
            param_id.name.data() as str,
            ptype_handle,
            &x.default,
            x.variadic) as *int8);
    }
    else
    {
        # Emplace a solid, unnamed parameter.
        types.push_ptr(code.make_parameter(
            (0 as *int8) as str,
            ptype_handle,
            code.make_nil(),
            x.variadic) as *int8);
    };

    # Return success.
    return true;
}