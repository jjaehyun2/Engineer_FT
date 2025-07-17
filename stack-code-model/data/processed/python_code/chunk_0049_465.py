class factory.Swf
{
	
var path_swf:String
	
	
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	
	function Swf(){
		if(ConfigurationSite.PATHWAY_TEMPLATE.length){
		path_swf=ConfigurationSite.PATHWAY_TEMPLATE
		}else{
		path_swf=""
		}
	}
	
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	
	function getSwf(template_:String):String{
		
		if(template_=="menuPrimary"){
			return path_swf+"menu_tree.swf";		
		}else if(template_=="banner"){
			return path_swf+"banner.swf";		
		}else if(template_=="slider"){
			return path_swf+"slider.swf";		
		}	else if(template_=="gallery"){
			return path_swf+"gallery.swf";		
		}
		else if(template_=="text"){
			return path_swf+"text.swf";
		}
		else if(template_=="newsy"){
			return path_swf+"newsy.swf";			
		}
		else if(template_=="form"){
			return path_swf+"form.swf";			
		}
		else if(template_=="player_mp3"){
			return path_swf+"player_mp3.swf"
		}
		else if(template_=="player_flv"){
			return path_swf+"player_flv.swf"
		}
		else if(template_=="book"){
			return path_swf+"book.swf"
		}
		else if(template_=="list"){
			return path_swf+"list.swf"
		}
		else if(template_=="calendar"){
			return path_swf+"calendar.swf"
		}
		else{
			return template_
		}
		
	}
		
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	
	
}