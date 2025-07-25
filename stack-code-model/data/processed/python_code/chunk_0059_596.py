package com.playfab.MultiplayerModels
{
    import com.playfab.PlayFabUtil;

    public class CreateBuildWithCustomContainerResponse
    {
        public var AreAssetsReadonly:*;
        public var BuildId:String;
        public var BuildName:String;
        public var ContainerFlavor:String;
        public var ContainerRunCommand:String;
        public var CreationTime:Date;
        public var CustomGameContainerImage:ContainerImageReference;
        public var GameAssetReferences:Vector.<AssetReference>;
        public var GameCertificateReferences:Vector.<GameCertificateReference>;
        public var Metadata:Object;
        public var MultiplayerServerCountPerVm:int;
        public var OsPlatform:String;
        public var Ports:Vector.<Port>;
        public var RegionConfigurations:Vector.<BuildRegion>;
        public var ServerType:String;
        public var UseStreamingForAssetDownloads:*;
        public var VmSize:String;

        public function CreateBuildWithCustomContainerResponse(data:Object=null)
        {
            if(data == null)
                return;
            AreAssetsReadonly = data.AreAssetsReadonly;
            BuildId = data.BuildId;
            BuildName = data.BuildName;
            ContainerFlavor = data.ContainerFlavor;
            ContainerRunCommand = data.ContainerRunCommand;
            CreationTime = PlayFabUtil.parseDate(data.CreationTime);
            CustomGameContainerImage = new ContainerImageReference(data.CustomGameContainerImage);
            if(data.GameAssetReferences) { GameAssetReferences = new Vector.<AssetReference>(); for(var GameAssetReferences_iter:int = 0; GameAssetReferences_iter < data.GameAssetReferences.length; GameAssetReferences_iter++) { GameAssetReferences[GameAssetReferences_iter] = new AssetReference(data.GameAssetReferences[GameAssetReferences_iter]); }}
            if(data.GameCertificateReferences) { GameCertificateReferences = new Vector.<GameCertificateReference>(); for(var GameCertificateReferences_iter:int = 0; GameCertificateReferences_iter < data.GameCertificateReferences.length; GameCertificateReferences_iter++) { GameCertificateReferences[GameCertificateReferences_iter] = new GameCertificateReference(data.GameCertificateReferences[GameCertificateReferences_iter]); }}
            Metadata = data.Metadata;
            MultiplayerServerCountPerVm = data.MultiplayerServerCountPerVm;
            OsPlatform = data.OsPlatform;
            if(data.Ports) { Ports = new Vector.<Port>(); for(var Ports_iter:int = 0; Ports_iter < data.Ports.length; Ports_iter++) { Ports[Ports_iter] = new Port(data.Ports[Ports_iter]); }}
            if(data.RegionConfigurations) { RegionConfigurations = new Vector.<BuildRegion>(); for(var RegionConfigurations_iter:int = 0; RegionConfigurations_iter < data.RegionConfigurations.length; RegionConfigurations_iter++) { RegionConfigurations[RegionConfigurations_iter] = new BuildRegion(data.RegionConfigurations[RegionConfigurations_iter]); }}
            ServerType = data.ServerType;
            UseStreamingForAssetDownloads = data.UseStreamingForAssetDownloads;
            VmSize = data.VmSize;

        }
    }
}