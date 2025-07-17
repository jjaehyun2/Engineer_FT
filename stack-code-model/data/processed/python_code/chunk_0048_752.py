package net.manaca.application.config
{
import flash.display.Stage;
import flash.events.EventDispatcher;
import flash.system.Security;

import net.manaca.errors.IllegalArgumentError;
import net.manaca.logging.LogLevel;
import net.manaca.logging.Tracer;
import net.manaca.logging.publishers.Output;
import net.manaca.logging.publishers.TracePublisher;

/**
 * The ApplicationInitHelper provide a base application configuration.
 * @author Sean Zou
 *
 */
public class ApplicationInitHelper extends EventDispatcher
{
    //==========================================================================
    //  Constructor
    //==========================================================================

    /**
     * Constructs a new <code>ApplicationInitHelper</code> instance.
     */
    public function ApplicationInitHelper()
    {
        super();
    }
    //==========================================================================
    //  Variables
    //==========================================================================
    private var stage:Stage;
    private var config:XML;
    //==========================================================================
    //  Methods
    //==========================================================================
    /**
     * 
     * @param stage
     * @param config
     * 
     */    
    public function init(stage:Stage, config:XML):void
    {
        if(stage != null)
        {
            this.stage = stage;
        }
        else
        {
            throw new IllegalArgumentError("invalid stage argument:" + stage);
        }
        
        this.config = config;
        
        initLogging();
        initSecurity();
    }
    
    private function initLogging():void
    {
        if(config.AppSettings.LoggingSettings.@enabled == "true")
        {
            setLogLevel();
            setPublishers();
        }
    }
    
    private function initSecurity():void
    {
        var info:XMLList = config.AppSettings.SecuritySettings;
        // configure cross domains
        for each(var url:String in info.CrossDomainPolicies.url)
        {
            Security.loadPolicyFile(url);
        }
        
        // configure allowed domains
        for each(var domain:String in info.AllowedDomains.domain)
        {
            Security.allowDomain(domain);
        }
    }
    
    private function setPublishers():void
    {
        var info:XMLList = config.AppSettings.LoggingSettings;
        
        if(info.TracePublisher != null)
        {
            var tracePublisher:TracePublisher = new TracePublisher();
            Tracer.logger.addPublisher(tracePublisher);
            tracePublisher.level = getLogLevel(info.TracePublisher.@logLevel);
        }
        
        if(info.Output != null && !Output.instance)
        {
            var output:Output = new Output(info.Output.@outputHeight, 
                info.Output.@strong);
            output.level = getLogLevel(info.Output.@logLevel);
            stage.addChild(output);
            stage.removeChild(output);
        }
    }
    
    private function setLogLevel():void
    {
        var info:XMLList = config.AppSettings.LoggingSettings;
        Tracer.logger.level = getLogLevel(info.@logLevel);
    }
    
    private function getLogLevel(level:String):LogLevel
    {
        var result:LogLevel = LogLevel.ALL;
        switch(level)
        {
            case LogLevelInfo.ALL:
            {
                result = LogLevel.ALL;
                break;
            }
            case LogLevelInfo.DEBUG:
            {
                result = LogLevel.DEBUG;
                break;
            }
            case LogLevelInfo.INFO:
            {
                result = LogLevel.INFO;
                break;
            }
            case LogLevelInfo.WARN:
            {
                result = LogLevel.WARN;
                break;
            }
            case LogLevelInfo.ERROR:
            {
                result = LogLevel.ERROR;
                break;
            }
            case LogLevelInfo.FATAL:
            {
                result = LogLevel.FATAL;
                break;
            }
            case LogLevelInfo.OFF:
            {
                result = LogLevel.OFF;
                break;
            }
            default:
            {
                result = LogLevel.OFF;
                break;
            }
        }
        return result;
    }
}
}