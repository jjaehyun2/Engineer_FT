package com.playfab
{
    import com.playfab.AdminModels.*;

    public class PlayFabAdminAPI
    {
        public static function AbortTaskInstance(request:AbortTaskInstanceRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:EmptyResponse = new EmptyResponse(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/AbortTaskInstance"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function AddLocalizedNews(request:AddLocalizedNewsRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:AddLocalizedNewsResult = new AddLocalizedNewsResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/AddLocalizedNews"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function AddNews(request:AddNewsRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:AddNewsResult = new AddNewsResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/AddNews"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function AddPlayerTag(request:AddPlayerTagRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:AddPlayerTagResult = new AddPlayerTagResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/AddPlayerTag"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function AddServerBuild(request:AddServerBuildRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:AddServerBuildResult = new AddServerBuildResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/AddServerBuild"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function AddUserVirtualCurrency(request:AddUserVirtualCurrencyRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:ModifyUserVirtualCurrencyResult = new ModifyUserVirtualCurrencyResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/AddUserVirtualCurrency"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function AddVirtualCurrencyTypes(request:AddVirtualCurrencyTypesRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:BlankResult = new BlankResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/AddVirtualCurrencyTypes"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function BanUsers(request:BanUsersRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:BanUsersResult = new BanUsersResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/BanUsers"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function CheckLimitedEditionItemAvailability(request:CheckLimitedEditionItemAvailabilityRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:CheckLimitedEditionItemAvailabilityResult = new CheckLimitedEditionItemAvailabilityResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/CheckLimitedEditionItemAvailability"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function CreateActionsOnPlayersInSegmentTask(request:CreateActionsOnPlayerSegmentTaskRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:CreateTaskResult = new CreateTaskResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/CreateActionsOnPlayersInSegmentTask"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function CreateCloudScriptTask(request:CreateCloudScriptTaskRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:CreateTaskResult = new CreateTaskResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/CreateCloudScriptTask"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function CreateInsightsScheduledScalingTask(request:CreateInsightsScheduledScalingTaskRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:CreateTaskResult = new CreateTaskResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/CreateInsightsScheduledScalingTask"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function CreateOpenIdConnection(request:CreateOpenIdConnectionRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:EmptyResponse = new EmptyResponse(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/CreateOpenIdConnection"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function CreatePlayerSharedSecret(request:CreatePlayerSharedSecretRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:CreatePlayerSharedSecretResult = new CreatePlayerSharedSecretResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/CreatePlayerSharedSecret"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function CreatePlayerStatisticDefinition(request:CreatePlayerStatisticDefinitionRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:CreatePlayerStatisticDefinitionResult = new CreatePlayerStatisticDefinitionResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/CreatePlayerStatisticDefinition"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function DeleteContent(request:DeleteContentRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:BlankResult = new BlankResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/DeleteContent"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function DeleteMasterPlayerAccount(request:DeleteMasterPlayerAccountRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:DeleteMasterPlayerAccountResult = new DeleteMasterPlayerAccountResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/DeleteMasterPlayerAccount"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function DeleteOpenIdConnection(request:DeleteOpenIdConnectionRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:EmptyResponse = new EmptyResponse(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/DeleteOpenIdConnection"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function DeletePlayer(request:DeletePlayerRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:DeletePlayerResult = new DeletePlayerResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/DeletePlayer"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function DeletePlayerSharedSecret(request:DeletePlayerSharedSecretRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:DeletePlayerSharedSecretResult = new DeletePlayerSharedSecretResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/DeletePlayerSharedSecret"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function DeleteStore(request:DeleteStoreRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:DeleteStoreResult = new DeleteStoreResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/DeleteStore"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function DeleteTask(request:DeleteTaskRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:EmptyResponse = new EmptyResponse(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/DeleteTask"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function DeleteTitle(request:DeleteTitleRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:DeleteTitleResult = new DeleteTitleResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/DeleteTitle"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function ExportMasterPlayerData(request:ExportMasterPlayerDataRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:ExportMasterPlayerDataResult = new ExportMasterPlayerDataResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/ExportMasterPlayerData"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetActionsOnPlayersInSegmentTaskInstance(request:GetTaskInstanceRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetActionsOnPlayersInSegmentTaskInstanceResult = new GetActionsOnPlayersInSegmentTaskInstanceResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetActionsOnPlayersInSegmentTaskInstance"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetAllSegments(request:GetAllSegmentsRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetAllSegmentsResult = new GetAllSegmentsResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetAllSegments"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetCatalogItems(request:GetCatalogItemsRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetCatalogItemsResult = new GetCatalogItemsResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetCatalogItems"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetCloudScriptRevision(request:GetCloudScriptRevisionRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetCloudScriptRevisionResult = new GetCloudScriptRevisionResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetCloudScriptRevision"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetCloudScriptTaskInstance(request:GetTaskInstanceRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetCloudScriptTaskInstanceResult = new GetCloudScriptTaskInstanceResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetCloudScriptTaskInstance"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetCloudScriptVersions(request:GetCloudScriptVersionsRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetCloudScriptVersionsResult = new GetCloudScriptVersionsResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetCloudScriptVersions"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetContentList(request:GetContentListRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetContentListResult = new GetContentListResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetContentList"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetContentUploadUrl(request:GetContentUploadUrlRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetContentUploadUrlResult = new GetContentUploadUrlResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetContentUploadUrl"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetDataReport(request:GetDataReportRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetDataReportResult = new GetDataReportResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetDataReport"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetMatchmakerGameInfo(request:GetMatchmakerGameInfoRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetMatchmakerGameInfoResult = new GetMatchmakerGameInfoResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetMatchmakerGameInfo"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetMatchmakerGameModes(request:GetMatchmakerGameModesRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetMatchmakerGameModesResult = new GetMatchmakerGameModesResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetMatchmakerGameModes"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetPlayedTitleList(request:GetPlayedTitleListRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetPlayedTitleListResult = new GetPlayedTitleListResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetPlayedTitleList"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetPlayerIdFromAuthToken(request:GetPlayerIdFromAuthTokenRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetPlayerIdFromAuthTokenResult = new GetPlayerIdFromAuthTokenResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetPlayerIdFromAuthToken"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetPlayerProfile(request:GetPlayerProfileRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetPlayerProfileResult = new GetPlayerProfileResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetPlayerProfile"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetPlayerSegments(request:GetPlayersSegmentsRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetPlayerSegmentsResult = new GetPlayerSegmentsResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetPlayerSegments"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetPlayerSharedSecrets(request:GetPlayerSharedSecretsRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetPlayerSharedSecretsResult = new GetPlayerSharedSecretsResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetPlayerSharedSecrets"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetPlayersInSegment(request:GetPlayersInSegmentRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetPlayersInSegmentResult = new GetPlayersInSegmentResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetPlayersInSegment"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetPlayerStatisticDefinitions(request:GetPlayerStatisticDefinitionsRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetPlayerStatisticDefinitionsResult = new GetPlayerStatisticDefinitionsResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetPlayerStatisticDefinitions"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetPlayerStatisticVersions(request:GetPlayerStatisticVersionsRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetPlayerStatisticVersionsResult = new GetPlayerStatisticVersionsResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetPlayerStatisticVersions"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetPlayerTags(request:GetPlayerTagsRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetPlayerTagsResult = new GetPlayerTagsResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetPlayerTags"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetPolicy(request:GetPolicyRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetPolicyResponse = new GetPolicyResponse(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetPolicy"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetPublisherData(request:GetPublisherDataRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetPublisherDataResult = new GetPublisherDataResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetPublisherData"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetRandomResultTables(request:GetRandomResultTablesRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetRandomResultTablesResult = new GetRandomResultTablesResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetRandomResultTables"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetServerBuildInfo(request:GetServerBuildInfoRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetServerBuildInfoResult = new GetServerBuildInfoResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetServerBuildInfo"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetServerBuildUploadUrl(request:GetServerBuildUploadURLRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetServerBuildUploadURLResult = new GetServerBuildUploadURLResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetServerBuildUploadUrl"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetStoreItems(request:GetStoreItemsRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetStoreItemsResult = new GetStoreItemsResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetStoreItems"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetTaskInstances(request:GetTaskInstancesRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetTaskInstancesResult = new GetTaskInstancesResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetTaskInstances"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetTasks(request:GetTasksRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetTasksResult = new GetTasksResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetTasks"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetTitleData(request:GetTitleDataRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetTitleDataResult = new GetTitleDataResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetTitleData"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetTitleInternalData(request:GetTitleDataRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetTitleDataResult = new GetTitleDataResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetTitleInternalData"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetUserAccountInfo(request:LookupUserAccountInfoRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:LookupUserAccountInfoResult = new LookupUserAccountInfoResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetUserAccountInfo"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetUserBans(request:GetUserBansRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetUserBansResult = new GetUserBansResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetUserBans"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetUserData(request:GetUserDataRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetUserDataResult = new GetUserDataResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetUserData"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetUserInternalData(request:GetUserDataRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetUserDataResult = new GetUserDataResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetUserInternalData"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetUserInventory(request:GetUserInventoryRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetUserInventoryResult = new GetUserInventoryResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetUserInventory"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetUserPublisherData(request:GetUserDataRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetUserDataResult = new GetUserDataResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetUserPublisherData"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetUserPublisherInternalData(request:GetUserDataRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetUserDataResult = new GetUserDataResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetUserPublisherInternalData"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetUserPublisherReadOnlyData(request:GetUserDataRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetUserDataResult = new GetUserDataResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetUserPublisherReadOnlyData"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GetUserReadOnlyData(request:GetUserDataRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GetUserDataResult = new GetUserDataResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GetUserReadOnlyData"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function GrantItemsToUsers(request:GrantItemsToUsersRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:GrantItemsToUsersResult = new GrantItemsToUsersResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/GrantItemsToUsers"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function IncrementLimitedEditionItemAvailability(request:IncrementLimitedEditionItemAvailabilityRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:IncrementLimitedEditionItemAvailabilityResult = new IncrementLimitedEditionItemAvailabilityResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/IncrementLimitedEditionItemAvailability"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function IncrementPlayerStatisticVersion(request:IncrementPlayerStatisticVersionRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:IncrementPlayerStatisticVersionResult = new IncrementPlayerStatisticVersionResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/IncrementPlayerStatisticVersion"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function ListOpenIdConnection(request:ListOpenIdConnectionRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:ListOpenIdConnectionResponse = new ListOpenIdConnectionResponse(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/ListOpenIdConnection"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function ListServerBuilds(request:ListBuildsRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:ListBuildsResult = new ListBuildsResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/ListServerBuilds"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function ListVirtualCurrencyTypes(request:ListVirtualCurrencyTypesRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:ListVirtualCurrencyTypesResult = new ListVirtualCurrencyTypesResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/ListVirtualCurrencyTypes"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function ModifyMatchmakerGameModes(request:ModifyMatchmakerGameModesRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:ModifyMatchmakerGameModesResult = new ModifyMatchmakerGameModesResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/ModifyMatchmakerGameModes"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function ModifyServerBuild(request:ModifyServerBuildRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:ModifyServerBuildResult = new ModifyServerBuildResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/ModifyServerBuild"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function RefundPurchase(request:RefundPurchaseRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:RefundPurchaseResponse = new RefundPurchaseResponse(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/RefundPurchase"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function RemovePlayerTag(request:RemovePlayerTagRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:RemovePlayerTagResult = new RemovePlayerTagResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/RemovePlayerTag"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function RemoveServerBuild(request:RemoveServerBuildRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:RemoveServerBuildResult = new RemoveServerBuildResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/RemoveServerBuild"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function RemoveVirtualCurrencyTypes(request:RemoveVirtualCurrencyTypesRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:BlankResult = new BlankResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/RemoveVirtualCurrencyTypes"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function ResetCharacterStatistics(request:ResetCharacterStatisticsRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:ResetCharacterStatisticsResult = new ResetCharacterStatisticsResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/ResetCharacterStatistics"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function ResetPassword(request:ResetPasswordRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:ResetPasswordResult = new ResetPasswordResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/ResetPassword"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function ResetUserStatistics(request:ResetUserStatisticsRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:ResetUserStatisticsResult = new ResetUserStatisticsResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/ResetUserStatistics"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function ResolvePurchaseDispute(request:ResolvePurchaseDisputeRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:ResolvePurchaseDisputeResponse = new ResolvePurchaseDisputeResponse(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/ResolvePurchaseDispute"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function RevokeAllBansForUser(request:RevokeAllBansForUserRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:RevokeAllBansForUserResult = new RevokeAllBansForUserResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/RevokeAllBansForUser"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function RevokeBans(request:RevokeBansRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:RevokeBansResult = new RevokeBansResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/RevokeBans"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function RevokeInventoryItem(request:RevokeInventoryItemRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:RevokeInventoryResult = new RevokeInventoryResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/RevokeInventoryItem"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function RevokeInventoryItems(request:RevokeInventoryItemsRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:RevokeInventoryItemsResult = new RevokeInventoryItemsResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/RevokeInventoryItems"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function RunTask(request:RunTaskRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:RunTaskResult = new RunTaskResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/RunTask"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function SendAccountRecoveryEmail(request:SendAccountRecoveryEmailRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:SendAccountRecoveryEmailResult = new SendAccountRecoveryEmailResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/SendAccountRecoveryEmail"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function SetCatalogItems(request:UpdateCatalogItemsRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:UpdateCatalogItemsResult = new UpdateCatalogItemsResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/SetCatalogItems"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function SetPlayerSecret(request:SetPlayerSecretRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:SetPlayerSecretResult = new SetPlayerSecretResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/SetPlayerSecret"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function SetPublishedRevision(request:SetPublishedRevisionRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:SetPublishedRevisionResult = new SetPublishedRevisionResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/SetPublishedRevision"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function SetPublisherData(request:SetPublisherDataRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:SetPublisherDataResult = new SetPublisherDataResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/SetPublisherData"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function SetStoreItems(request:UpdateStoreItemsRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:UpdateStoreItemsResult = new UpdateStoreItemsResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/SetStoreItems"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function SetTitleData(request:SetTitleDataRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:SetTitleDataResult = new SetTitleDataResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/SetTitleData"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function SetTitleInternalData(request:SetTitleDataRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:SetTitleDataResult = new SetTitleDataResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/SetTitleInternalData"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function SetupPushNotification(request:SetupPushNotificationRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:SetupPushNotificationResult = new SetupPushNotificationResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/SetupPushNotification"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function SubtractUserVirtualCurrency(request:SubtractUserVirtualCurrencyRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:ModifyUserVirtualCurrencyResult = new ModifyUserVirtualCurrencyResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/SubtractUserVirtualCurrency"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function UpdateBans(request:UpdateBansRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:UpdateBansResult = new UpdateBansResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/UpdateBans"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function UpdateCatalogItems(request:UpdateCatalogItemsRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:UpdateCatalogItemsResult = new UpdateCatalogItemsResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/UpdateCatalogItems"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function UpdateCloudScript(request:UpdateCloudScriptRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:UpdateCloudScriptResult = new UpdateCloudScriptResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/UpdateCloudScript"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function UpdateOpenIdConnection(request:UpdateOpenIdConnectionRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:EmptyResponse = new EmptyResponse(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/UpdateOpenIdConnection"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function UpdatePlayerSharedSecret(request:UpdatePlayerSharedSecretRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:UpdatePlayerSharedSecretResult = new UpdatePlayerSharedSecretResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/UpdatePlayerSharedSecret"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function UpdatePlayerStatisticDefinition(request:UpdatePlayerStatisticDefinitionRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:UpdatePlayerStatisticDefinitionResult = new UpdatePlayerStatisticDefinitionResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/UpdatePlayerStatisticDefinition"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function UpdatePolicy(request:UpdatePolicyRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:UpdatePolicyResponse = new UpdatePolicyResponse(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/UpdatePolicy"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function UpdateRandomResultTables(request:UpdateRandomResultTablesRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:UpdateRandomResultTablesResult = new UpdateRandomResultTablesResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/UpdateRandomResultTables"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function UpdateStoreItems(request:UpdateStoreItemsRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:UpdateStoreItemsResult = new UpdateStoreItemsResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/UpdateStoreItems"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function UpdateTask(request:UpdateTaskRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:EmptyResponse = new EmptyResponse(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/UpdateTask"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function UpdateUserData(request:UpdateUserDataRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:UpdateUserDataResult = new UpdateUserDataResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/UpdateUserData"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function UpdateUserInternalData(request:UpdateUserInternalDataRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:UpdateUserDataResult = new UpdateUserDataResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/UpdateUserInternalData"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function UpdateUserPublisherData(request:UpdateUserDataRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:UpdateUserDataResult = new UpdateUserDataResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/UpdateUserPublisherData"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function UpdateUserPublisherInternalData(request:UpdateUserInternalDataRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:UpdateUserDataResult = new UpdateUserDataResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/UpdateUserPublisherInternalData"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function UpdateUserPublisherReadOnlyData(request:UpdateUserDataRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:UpdateUserDataResult = new UpdateUserDataResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/UpdateUserPublisherReadOnlyData"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function UpdateUserReadOnlyData(request:UpdateUserDataRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:UpdateUserDataResult = new UpdateUserDataResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/UpdateUserReadOnlyData"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

        public static function UpdateUserTitleDisplayName(request:UpdateUserTitleDisplayNameRequest, onComplete:Function, onError:Function):void
        {
            if (PlayFabSettings.DeveloperSecretKey == null) throw new Error ("Must have PlayFabSettings.DeveloperSecretKey set to call this method");
            var requetJson:String = JSON.stringify( request );

            var onPostComplete:Function = function(resultData:Object, error:PlayFabError):void
            {
                if(error)
                {
                    if(onError != null)
                        onError(error);
                    if(PlayFabSettings.GlobalErrorHandler != null)
                        PlayFabSettings.GlobalErrorHandler(error);
                }
                else
                {
                    var result:UpdateUserTitleDisplayNameResult = new UpdateUserTitleDisplayNameResult(resultData);

                    if(onComplete != null)
                        onComplete(result);
                }
            }

            PlayFabHTTP.post(PlayFabSettings.GetURL("/Admin/UpdateUserTitleDisplayName"), requetJson, "X-SecretKey", PlayFabSettings.DeveloperSecretKey, onPostComplete);
        }

    }
}