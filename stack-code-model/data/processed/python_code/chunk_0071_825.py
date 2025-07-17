package cn.geckos.shuttle.views
{
import __AS3__.vec.Vector;

import cn.geckos.crazyas.utils.SizeFormat;
import cn.geckos.shuttle.Notices;
import cn.geckos.shuttle.models.vo.ImageVO;
import cn.geckos.shuttle.property.BooleanEditor;
import cn.geckos.shuttle.property.DefaultPropertyModel;
import cn.geckos.shuttle.property.EnumEditor;
import cn.geckos.shuttle.property.MultipleObjectsPropertyModel;
import cn.geckos.shuttle.property.PropertyManager;
import cn.geckos.shuttle.property.StringEditor;
import cn.geckos.shuttle.views.components.ImageListBox;
import cn.geckos.shuttle.views.components.ImageSettingsPanel;

import flash.desktop.ClipboardFormats;
import flash.desktop.NativeDragActions;
import flash.desktop.NativeDragManager;
import flash.events.FileListEvent;
import flash.events.MouseEvent;
import flash.events.NativeDragEvent;
import flash.filesystem.File;
import flash.net.FileFilter;

import mx.events.CollectionEvent;
import mx.events.ListEvent;
import mx.events.MenuEvent;
import mx.resources.ResourceManager;

import org.puremvc.as3.interfaces.INotification;
import org.puremvc.as3.patterns.mediator.Mediator;

public class ImageListMediator extends Mediator
{
    
    public static const NAME:String = 'ImageListMediator';
    
    /**
     * 允许选择的图片文件格式
     */
    private static var imageTypeFilter:Array = [
        new FileFilter("Images(*.jpg;*.gif;*.png;*.bmp)", "*.jpg;*.gif;*.png;*.bmp"),
    ];
    
    /**
     * 用来选择图片文件的File对象 
     */    
    private var _file:File;
    
    protected var imageProMgr:PropertyManager;
    
    
    public function get component():ImageListBox
    {
        return viewComponent as ImageListBox;
    }
    
    /**
     * Constructor 
     * @param mediatorName
     * @param viewComponent
     * 
     */
    public function ImageListMediator(mediatorName:String=null, viewComponent:Object=null)
    {
        super(mediatorName, viewComponent);
        
        component.addImgBtn.addEventListener(MouseEvent.CLICK, addImgBtnClickHandler);
        component.uploadBtn.addEventListener(MenuEvent.ITEM_CLICK, uploadBtnClickHandler);
        component.removeBtn.addEventListener(MenuEvent.ITEM_CLICK, removeBtnClickHandler);
        
        component.list.addEventListener(ListEvent.CHANGE, listChangeHandler);
        component.list.addEventListener(NativeDragEvent.NATIVE_DRAG_ENTER, dragEnterHandler);
        component.list.addEventListener(NativeDragEvent.NATIVE_DRAG_DROP, dragDropHandler);
        
        component.listData.addEventListener(CollectionEvent.COLLECTION_CHANGE, dataChangeHandler);
    }
    
    private function getFile():File
    {
        if( !_file ) {
            _file = new File();
            _file.addEventListener(FileListEvent.SELECT_MULTIPLE, fileSelectMultipleHandler);
        }
        return _file;
    }
    
    public function addFilesToList(files:Vector.<File>):void
    {
        for each( var file:File in files ) 
        {
            var fileExist:Boolean;
            for each( var vo:ImageVO in component.listData )
            {
                if( file.nativePath == File(vo.file).nativePath ) {
                    fileExist = true;
                }
            }
            
            if( !fileExist ) {
                component.listData.addItem(new ImageVO(file));
            }
            
        }
    }
    
    
    /**
     * 浏览图片文件
     */
    private function addImgBtnClickHandler(event:MouseEvent):void
    {
        getFile().browseForOpenMultiple('Select images for upload.', imageTypeFilter);
    }
    
    /**
     * 选择文件后把图片添加到列表中
     */
    private function fileSelectMultipleHandler(event:FileListEvent):void
    {
        addFilesToList(Vector.<File>(event.files));
    }
    
    /**
     * 上传按钮事件
     * 
     */
    private function uploadBtnClickHandler(event:MenuEvent):void
    {
        var data:Object;
        
        // 单击按钮菜单上传全部
        if (event.index == 1) 
        {
            data = component.listData;
        }
        else  // 单击按钮上传选中的照片
        {
            data = component.list.selectedItems;
        }
        
        for each( var vo:ImageVO in data )
        {
            if (vo.state == ImageVO.NOT_UPLOAD) 
            {
                sendNotification(Notices.UPLOAD, vo);
            }
        }
    }
    
    /**
     * 删除按钮事件
     * 
     */
    private function removeBtnClickHandler(event:MenuEvent):void
    {
        // 单击按钮删除选中的图片
        var data:Object = component.list.selectedItems;
        
        // 单击按菜单钮删除上传图片
        if (event.index == 1) 
        {
            data = component.listData;
        }
        
        // 停止正在上传的文件
        for each (var vo:ImageVO in component.list.selectedItems)
        {
            if (vo.state == ImageVO.UPLOADING) 
            {
                vo.cancelUpload();
            }
        }
        
        if (event.index == 0) 
        {
	        component.removeSelectedItems();
        }
        else 
        {
            component.listData.removeAll();
        }
    }
    
    /**
     * image list selection change
     */
    private function listChangeHandler(event:ListEvent):void
    {
        //FIXME very dirty, to be refactory
        
        if (!imageProMgr) 
        {
            imageProMgr = new PropertyManager();
            
            var panel:ImageSettingsPanel = component.settingsPanel
            
            imageProMgr.setEditor(new StringEditor(panel.titleInput), 'title');
            imageProMgr.setEditor(new StringEditor(panel.descInput), 'description');
            imageProMgr.setEditor(new StringEditor(panel.tagsInput), 'tags');
            imageProMgr.setEditor(new EnumEditor(panel.mainPrivacy), 'isPublic');
            imageProMgr.setEditor(new BooleanEditor(panel.friCheck), 'isFriends');
            imageProMgr.setEditor(new BooleanEditor(panel.fmlCheck), 'isFamily');
            
            imageProMgr.setEditor(new EnumEditor(panel.safetyCombo), 'safety');
            imageProMgr.setEditor(new EnumEditor(panel.hiddenCombo), 'hidden');
            imageProMgr.setEditor(new EnumEditor(panel.contentCombo), 'content');
        }
        
        var editorOwner:Object;
        var modelCls:Class;
        
        if (component.list.selectedItems.length == 1) 
        {
            var data:Object = component.list.selectedItem;
            if (data['isPublic'] == undefined) 
            {
                data['isPublic'] = true;
            }
            editorOwner = data;
            modelCls = DefaultPropertyModel;
            
        }
        else if (component.list.selectedItems.length > 1)
        {
            editorOwner = component.list.selectedItems;
            modelCls = MultipleObjectsPropertyModel;
        }
        imageProMgr.getEditor('title').bindTo(new modelCls(editorOwner, 'title'));
        imageProMgr.getEditor('description').bindTo(new modelCls(editorOwner, 'description'));
        imageProMgr.getEditor('tags').bindTo(new modelCls(editorOwner, 'tags'));
        imageProMgr.getEditor('isPublic').bindTo(new modelCls(editorOwner, 'isPublic'));
        imageProMgr.getEditor('isFriends').bindTo(new modelCls(editorOwner, 'isFriends'));
        imageProMgr.getEditor('isFamily').bindTo(new modelCls(editorOwner, 'isFamily'));
        
        imageProMgr.getEditor('safety').bindTo(new modelCls(editorOwner, 'safety'));
        imageProMgr.getEditor('hidden').bindTo(new modelCls(editorOwner, 'hidden'));
        imageProMgr.getEditor('content').bindTo(new modelCls(editorOwner, 'content'));
    }
    
    private function dataChangeHandler(event:CollectionEvent):void
    {
        var numPhotos:Number = component.listData.length;
        var size:Number = 0;
        var numUploaded:Number = 0
        for each(var vo:ImageVO in component.listData)
        {
            size += vo.file.size;
            if (vo.state == ImageVO.UPLOADED)
            {
                numUploaded++;
            }
        }
        component.photoStat.text = 
            ResourceManager.getInstance().getString('lang', 'photoStat', 
                        [numPhotos, SizeFormat.humanRead(size), numUploaded]);
    }
    
    //
    // drag and drop event
    //
    
    private function dragEnterHandler(event:NativeDragEvent):void
    {
        NativeDragManager.acceptDragDrop(component.list);
    }
    
    private function dragDropHandler(event:NativeDragEvent):void
    {
        try
        {
            NativeDragManager.dropAction = NativeDragActions.COPY;
            var files:Vector.<File> = 
                Vector.<File>( event.clipboard.getData(ClipboardFormats.FILE_LIST_FORMAT) );
            addFilesToList(files);
        }
        catch(error:Error)
        {
            // do nothing yet
        }
    }
    
    
    //
    // puremvc functions 
    //
    
    override public function listNotificationInterests():Array
    {
        return [
            Notices.CHECK_FLICKR_TOKEN_OK,
            Notices.GET_FLICKR_AUTH_TOKEN_SUCCESS,
        ];
    }
    
    override public function handleNotification(notification:INotification):void
    {
        switch( notification.getName() )
        {
            case Notices.CHECK_FLICKR_TOKEN_OK:
            case Notices.GET_FLICKR_AUTH_TOKEN_SUCCESS:
                component.enabled = true;
                break;
        }
    }
        
}
}