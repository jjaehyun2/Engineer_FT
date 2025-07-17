package com.base.module.interfaces
{
	import com.base.events.interfaces.IDispatcher;
	
	/**
	 * 模块定义框架
	 * @author movinliao
	 * 
	 */
	public interface IModule extends IDispatcher
	{
		/**
		 * 模块初始化
		 * @param api
		 * 
		 */
		function init(api: *): void;
		/**
		 *模块销毁 
		 * 
		 */
		function destroy(): void;
		/**
		 *停止 
		 * 
		 */
		function stop(): void;
		/**
		 *开始 
		 * 
		 */
		function start(): void;
		/**
		 * 增加块
		 * @param key
		 * @param block
		 * 
		 */
		function addBlock(key: String, block: IBlock): void;
		/**
		 * 移除块
		 * @param key
		 * 
		 */
		function removeBlock(key: String): void;
		/**
		 *获取块 
		 * @param key
		 * @return 
		 * 
		 */
		function block(key: String): IBlock;
		/**
		 *判断是否已经加载
		 * @return Boolean
		 * 
		 */
		function hasBlock(key: String): Boolean;
		/**
		 *获取是否已经初始化 
		 * @return 
		 * 
		 */
		function get inited():Boolean;
		/**
		 * 获取api
		 * @return 
		 * 
		 */
		function get api(): *;
		/**
		 *获取模块键值组 
		 * @return 
		 * 
		 */
		function get keys(): Array;
		/**
		 * 关注某块事件
		 * @param blockKey 块标志
		 * @param key 事件标志
		 * @param listener 事件
		 * @param priority 优先级
		 * 
		 */
		function addBlockListener(blockKey: String, key: String, listener: Function, priority:int = 0): void;
		/**
		 *移除块事件关注 
		 * @param blockKey 块标志
		 * @param key 事件标志
		 * @param listener 事件
		 * @param priority 优先级
		 * 
		 */
		function removeBlockListener(blockKey: String, key: String, listener: Function, priority:int = 0):void;
		/**
		 *记录日志 
		 * @param content
		 * @param type
		 * @return 
		 * 
		 */
		function log(content: String, priority: *): void;
	}
}