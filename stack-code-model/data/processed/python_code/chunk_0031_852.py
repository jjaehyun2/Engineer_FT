package com.base.module.interfaces
{
	import com.base.db.interfaces.ITable;
	
	import flash.utils.ByteArray;

	/**
	 * 带数据段模块定义框架
	 * @author movinliao
	 * 
	 */
	public interface IDataModule extends IModule
	{
		/**
		 *获取模块的区块数据 
		 * @return 
		 * 
		 */
		function get table(): ITable;
		/**
		 *注册proto事件 
		 * @param appid
		 * @param uri
		 * @param handler
		 * @param priority
		 * 
		 */
		function addProto(appid: uint, uri: uint, handler:Function, priority:int=0): void;
		/**
		 *反注册proto事件 
		 * @param appid
		 * @param uri
		 * @param handler
		 * @param priority
		 * 
		 */
		function removeProto(appid: uint, uri: uint, handler:Function, priority:int=0): void;
		/**
		 *发送数据 
		 * @param uri
		 * @param data
		 * @param retry
		 * 
		 */
		function send(appid: uint, uri: uint, retry: Boolean, merger: Function, ...args): Boolean;
		/**
		 *校验回包 
		 * @param appid
		 * @param resCode
		 * @return 
		 * 
		 */
		function response(appid:uint, sequence: Number, resCode: int, resMsg:String): Boolean;
		/**
		 * 执行某块指令
		 * @param key: 块标志
		 * @param cmd: 指令标志
		 * @param args: 参数
		 * @return: 
		 */
	   function excute(key: String, cmd: String, args: Array = null): *;
	   /**
		* 获取某块字段值
		* @param key: 块标志
		* @param fieldId: 字段
		* @return: 
		*/
	   function field(key: String, fieldType: uint, fieldId: uint): *;
	   /**
	    *提示框触发 
	    * @param type 提示类型
	    * @param id  触发标志id
	    * @param extra 额外数据
	    * 
	    */
	   function trigerBox(type: uint, id: uint, extra: * = null): void;
	   /**
	    * 执行
	    * @param key 标志
	    * @param param 参数
	    * 
	    */
	   function invoke(key: uint, param: * = null):void;
	   /**
	    *添加通知 
	    * @param key 标志
	    * @param param 附带数据
	    * @param times 次数
	    * @param active 是否激活
	    * @param cover 是否覆盖
	    */
	   function pushNotify(key: uint, param: * = null, times: uint = 0, active: Boolean = false, cover: Boolean = false): void;
	}
}