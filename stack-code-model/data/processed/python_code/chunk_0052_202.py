//用户更新已提交的拓扑

import Components.Controller;
import Components.Host;
import Components.Link;
import Components.Switch;

import mx.collections.ArrayCollection;

import vo.Vnet_controller;
import vo.Vnet_executor_vnet;
import vo.Vnet_host;
import vo.Vnet_instance_host;
import vo.Vnet_link;
import vo.Vnet_oflink;
import vo.Vnet_ofport;
import vo.Vnet_request;
import vo.Vnet_switch;
import vo.Vnet_switch_ofport;
import vo.Vnet_vnet;
import vo.Vnet_vnet_resource;

/*	Request Type      Meaning          vnet ID      Content ID
	1             	Create Vnet           *              -
	2          		Delete Vnet           *              -
	3          		Create Vhost          *           Host ID
	4          		Delete Vhost    	  *           Host ID
	5          		Create Vswitch     	  *           Switch ID
	6         		Delete Vswitch     	  *           Switch ID
	7          		Create Vcontroller    *           Controller ID
	8          		Delete Vcontroller    *           Controller ID
	9          		Create Vlink      	  *           Link ID
	10         		Delete Vlink   	      *           Link ID
	11				Create oflink 		  *			  oflink ID
	12				Delete oflink         *           oflink ID
	
*/
protected function vnet_update_clickHandler(event:MouseEvent):void {
	var date:Date = new Date();
	var tmplist:ArrayCollection = new ArrayCollection();
	var update_vnet_id:String = vnet_vnet.vnet_id;
	var tmp_executor_vnet:Vnet_executor_vnet = null;
	var myvnet:Vnet_vnet = null;
	var is_delete:Boolean = false;
	var vnet_add_oflinks:ArrayCollection = new ArrayCollection();
	var vnet_add_links:ArrayCollection = new ArrayCollection();
	var vnet_add_resources:ArrayCollection = new ArrayCollection();
	var vnet_add_instances:ArrayCollection = new ArrayCollection();
	var vnet_add_ins_flavor:ArrayCollection = new ArrayCollection();
	var vnet_add_ins_image:ArrayCollection = new ArrayCollection();
	var vnet_add_ins_con:ArrayCollection = new ArrayCollection();
	var vnet_add_ins_host:ArrayCollection = new ArrayCollection();
	var tmp_swi_ops:ArrayCollection = new ArrayCollection();
	for(var tmp:int=0; tmp<vnet_switch_ofports.length; tmp++){
		tmp_swi_ops.addItem(vnet_switch_ofports[tmp]);
	}
	
	//request_type =2，delete vnet
	if(C_obj.length<1 && H_obj.length<1 && S_obj.length<1){
		is_delete = true;
		var del_vnet_requests:ArrayCollection = new ArrayCollection();
		var del_vnet_req:Vnet_request = new Vnet_request("Delete Vnet","2",null,vnet_vnet.vnet_id,executor_name + "~" +date.toString());
		vnet_requests.addItem(del_vnet_req);
		vnet_controllers.removeAll();
		vnet_switches.removeAll();
		vnet_hosts.removeAll();
		vnet_oflinks.removeAll();
		vnet_links.removeAll();
		vnet_ofports.removeAll();
		vnet_switch_ofports.removeAll();
		vnet_vnet = null;
		link_num = 0;
		vnet_counter_vnet = 0;
		vnet_counter = 0;
		vnet_counter_ofport = 0;
	}//end type 2
	
	if(!is_delete){
		//request_type =8, delete controller
		var del_con_req:Vnet_request;
		for(var vc_num8:int=0;vc_num8<vnet_del_cons.length;vc_num8++){
			del_con_req = new Vnet_request("Delete Virtual Controller","8",vnet_vnet.vnet_id,vnet_del_cons[vc_num8].controller_id,executor_name + "~" +date.toString());
			vnet_requests.addItem(del_con_req);
			for(var v_cons:int=0; v_cons<vnet_controllers.length; v_cons++){
				if(vnet_controllers[v_cons].controller_id == vnet_del_cons[vc_num8].controller_id){
					vnet_controllers.removeItemAt(v_cons);
					break;
				}
			}
		}
		
		//request_type =7, add controller
		var add_con_req:Vnet_request;
		for(var vc_num7:int=0; vc_num7<vnet_add_cons.length; vc_num7++){
			add_con_req = new Vnet_request("Add Virtual Controller","7",vnet_vnet.vnet_id,vnet_add_cons[vc_num7].controller_id,executor_name + "~" +date.toString());
			vnet_requests.addItem(add_con_req);
			vnet_controllers.addItem(vnet_add_cons[vc_num7]);
			
			for(var item_con:int=0; item_con<C_obj.length; item_con++){
				if(C_obj[item_con].getCon_id() == vnet_add_cons[vc_num7].controller_id){
					
					var ins:Vnet_instance = new Vnet_instance();
					ins.instance_id = "instance~" + vnet_counter_instance +"~"+ C_obj[item_con].getTime() +"~"+ executor_name;
					ins.instance_status = "wait";
					ins.instance_type = "Controller";
					vnet_instances.addItem(ins);
					vnet_add_instances.addItem(ins);
					vnet_counter_instance++;
					
					var flavor_ins:Vnet_flavor_instance = new Vnet_flavor_instance();
					flavor_ins.instance_id = ins.instance_id;
					flavor_ins.flavor_id = C_obj[item_con].getflavor();
					if(flavor_ins.flavor_id == -1){
						for(var d0:int=0; d0<vnet_flavors.length; d0++){
							if(vnet_flavors.getItemAt(d0).flavor_name == "m1.small"){
								flavor_ins.flavor_id = vnet_flavors.getItemAt(d0).flavor_id;
								C_obj[item_con].setflavor(vnet_flavors.getItemAt(d0).flavor_id);
								break;
							}
						}
					}
					vnet_flavor_instance.addItem(flavor_ins);
					vnet_add_ins_flavor.addItem(flavor_ins);
					
					var image_ins:Vnet_image_instance = new Vnet_image_instance();
					image_ins.instance_id = ins.instance_id;
					image_ins.image_id = C_obj[item_con].getimage();
					if(image_ins.image_id == -1){
						for(var d1:int=0; d1<vnet_images.length; d1++){
							if(vnet_images.getItemAt(d1).image_name == "floodlight"){
								image_ins.image_id = vnet_images.getItemAt(d1).image_id;
								C_obj[item_con].setimage(vnet_images.getItemAt(d1).image_id);
								break;
							}
						}
					}
					vnet_image_instance.addItem(image_ins);
					vnet_add_ins_image.addItem(image_ins);
					
					var ins_con:Vnet_instance_controller = new Vnet_instance_controller();
					ins_con.controller_id = vnet_add_cons[vc_num7].controller_id;
					ins_con.instance_id = ins.instance_id;
					vnet_instance_controller.addItem(ins_con);
					vnet_add_ins_con.addItem(ins_con);
					
					var v_res:Vnet_vnet_resource = new Vnet_vnet_resource();
					v_res.resource_id = vnet_add_cons[vc_num7].controller_id;
					v_res.vnet_id = vnet_vnet.vnet_id;
					v_res.resource_type = "Controller";
					v_res.resource_status = "wait";
					v_res.resource_timestamp = C_obj[item_con].getTime();
					vnet_add_resources.addItem(v_res);
					vnet_resources.addItem(v_res);
					
					break;
				}
			}
		}
		
		//request_type =4, delete host
		var del_host_req:Vnet_request;
		for(var vh_num4:int=0; vh_num4<vnet_del_hosts.length; vh_num4++){
			del_host_req = new Vnet_request("Delete Virtual Host","4",vnet_vnet.vnet_id,vnet_del_hosts[vh_num4].host_id,executor_name + "~" +date.toString());
			vnet_requests.addItem(del_host_req);
			for(var v_hosts:int=0; v_hosts<vnet_hosts.length; v_hosts++){
				if(vnet_hosts[v_hosts].host_id == vnet_del_hosts[vh_num4].host_id){
					vnet_hosts.removeItemAt(v_hosts);
					break;
				}
			}
		}
		
		//request_type =3, add host
		var add_host_req:Vnet_request;
		for(var vh_num3:int=0; vh_num3<vnet_add_hosts.length; vh_num3++){
			add_host_req = new Vnet_request("Add Virtual Host","3",vnet_vnet.vnet_id,vnet_add_hosts[vh_num3].host_id,executor_name + "~" +date.toString());
			vnet_requests.addItem(add_host_req);
			vnet_hosts.addItem(vnet_add_hosts[vh_num3]);
			
			for(var item_hos:int=0; item_hos<H_obj.length; item_hos++){
				if(Host(H_obj[item_hos]).getHost_ID() == vnet_add_hosts[vh_num3].host_id){
					
					var ins2:Vnet_instance = new Vnet_instance();
					ins2.instance_id = "instance~" + vnet_counter_instance +"~"+ H_obj[item_hos].getTime() +"~"+ executor_name;
					ins2.instance_status = "wait";
					ins2.instance_type = "Host";
					vnet_instances.addItem(ins2);
					vnet_add_instances.addItem(ins2);
					vnet_counter_instance++;
					
					var flavor_ins2:Vnet_flavor_instance = new Vnet_flavor_instance();
					flavor_ins2.instance_id = ins2.instance_id;
					flavor_ins2.flavor_id = H_obj[item_hos].getflavor();
					if(flavor_ins2.flavor_id == -1){
						for(var d2:int=0; d2<vnet_flavors.length; d2++){
							if(vnet_flavors.getItemAt(d2).flavor_name == "m1.nano"){
								flavor_ins2.flavor_id = vnet_flavors.getItemAt(d2).flavor_id;
								H_obj[item_hos].setflavor(vnet_flavors.getItemAt(d2).flavor_id);
								break;
							}
						}
					}
					vnet_flavor_instance.addItem(flavor_ins2);
					vnet_add_ins_flavor.addItem(flavor_ins2);
					
					var image_ins2:Vnet_image_instance = new Vnet_image_instance();
					image_ins2.instance_id = ins2.instance_id;
					image_ins2.image_id = H_obj[item_hos].getimage();
					if(image_ins2.image_id == -1){
						for(var d3:int=0; d3<vnet_images.length; d3++){
							if(vnet_images.getItemAt(d3).image_name == "cirros-0.3.4-x86_64"){
								image_ins2.image_id = vnet_images.getItemAt(d3).image_id;
								H_obj[item_hos].setimage(vnet_images.getItemAt(d3).image_id);
								break;
							}
						}
					}
					vnet_image_instance.addItem(image_ins2);
					vnet_add_ins_image.addItem(image_ins2);
					
					var ins_con2:Vnet_instance_host = new Vnet_instance_host();
					ins_con2.host_id = vnet_add_hosts[vh_num3].host_id;
					ins_con2.instance_id = ins2.instance_id;
					vnet_instance_host.addItem(ins_con2);
					vnet_add_ins_host.addItem(ins_con2);
					
					var v_res2:Vnet_vnet_resource = new Vnet_vnet_resource();
					v_res2.resource_id = vnet_add_hosts[vh_num3].host_id;
					v_res2.vnet_id = vnet_vnet.vnet_id;
					v_res2.resource_type = "Host";
					v_res2.resource_status = "wait";
					v_res2.resource_timestamp = H_obj[item_hos].getTime();
					vnet_add_resources.addItem(v_res2);
					vnet_resources.addItem(v_res2);
					
					break;
				}
			}
		}
		
		//request_type 6, delete switch
		var del_swi_req:Vnet_request;
		for(var vs_num6:int=0; vs_num6<vnet_del_swis.length; vs_num6++){
			del_swi_req = new Vnet_request("Delete Virtual Switch","6",vnet_vnet.vnet_id,vnet_del_swis[vs_num6].switch_id,executor_name + "~" +date.toString());
			vnet_requests.addItem(del_swi_req);
			for(var v_swis:int=0; v_swis<vnet_switches.length; v_swis++){
				if(vnet_switches[v_swis].switch_id == vnet_del_swis[vs_num6].switch_id){
					vnet_switches.removeItemAt(v_swis);
					break;
				}
			}
		}
		
		//request_type =5, add switch
		var add_swi_req:Vnet_request;
		for(var vs_num5:int=0; vs_num5<vnet_add_swis.length; vs_num5++){
			add_swi_req = new Vnet_request("Add Virtual Switch","5",vnet_vnet.vnet_id,vnet_add_swis[vs_num5].switch_id,executor_name + "~" +date.toString());
			vnet_requests.addItem(add_swi_req);
			vnet_switches.addItem(vnet_add_swis[vs_num5]);
			
			var v_res3:Vnet_vnet_resource = new Vnet_vnet_resource();
			v_res3.resource_id = vnet_add_swis[vs_num5].switch_id;
			v_res3.vnet_id = vnet_vnet.vnet_id;
			v_res3.resource_type = "Switch";
			v_res3.resource_status = "wait";
			var temp:Array = v_res3.resource_id.split("~");
			v_res3.resource_timestamp = temp[2];
			vnet_resources.addItem(v_res3);
			vnet_add_resources.addItem(v_res3);
		}
		
		//request_type =9, add link && request_type =10, delete link 
		var link_req:Vnet_request;
		for(var vl_num10:int=0; vl_num10<vnet_updatelinks.length; vl_num10++){
			if(vnet_updatelinks[vl_num10].status == "add"){
				var id_tmp:Array = vnet_updatelinks[vl_num10].link_id.split("~");
				
				if(id_tmp[0] == "oflink"){ //oflink
					//add oflink
					var add_ol:Vnet_oflink = new Vnet_oflink();
					add_ol.oflink_id = vnet_updatelinks[vl_num10].link_id;
					add_ol.oflink_status = "wait";
					if(vnet_updatelinks[vl_num10].fromObj.className == "Controller"){
						add_ol.controller_id = Controller(vnet_updatelinks[vl_num10].fromObj).getCon_id();
						add_ol.switch_id = Switch(vnet_updatelinks[vl_num10].toObj).getSwitch_id();
					}
					else{
						add_ol.controller_id = Controller(vnet_updatelinks[vl_num10].toObj).getCon_id();
						add_ol.switch_id = Switch(vnet_updatelinks[vl_num10].fromObj).getSwitch_id();
					}
					vnet_add_oflinks.addItem(add_ol);
					vnet_oflinks.addItem(add_ol);
					//add resource
					var v_res4:Vnet_vnet_resource = new Vnet_vnet_resource();
					v_res4.resource_id = add_ol.oflink_id;
					v_res4.vnet_id = vnet_vnet.vnet_id;
					v_res4.resource_type = "oflink";
					v_res4.resource_status = "wait";
					var temp2:Array = v_res4.resource_id.split("~");
					v_res4.resource_timestamp = temp2[2];
					vnet_add_resources.addItem(v_res4);
					
					link_req = new Vnet_request("Add oflink","11",vnet_vnet.vnet_id,vnet_updatelinks[vl_num10].link_id,executor_name + "~" +date.toString());
				}
				
				else{  //link 
					//add link
					var add_l:Vnet_link = new Vnet_link();
					add_l.link_id = vnet_updatelinks[vl_num10].link_id;
					add_l.link_status = "wait";
					add_l.link_bandwidth = 0;
					if(vnet_updatelinks[vl_num10].fromObj.className == "Switch"){
						add_l.link_src_id = Switch(vnet_updatelinks[vl_num10].fromObj).getSwitch_id();
						add_l.link_src_type = "Switch";
						var swi_isnew:Boolean = false;
						for(var s_num1:int=0; s_num1<vnet_add_swis.length; s_num1++){
							if(vnet_add_swis[s_num1].switch_id == add_l.link_src_id){
								swi_isnew = true;
							}
						}
						if(swi_isnew) {
							//add ofport
							var n1:int = 1;
							for(var s_op_num1:int=0;s_op_num1<tmp_swi_ops.length;s_op_num1++){
								if(tmp_swi_ops[s_op_num1].switch_id == add_l.link_src_id){
									n1++;
								}
							}
							var add_op1:Vnet_ofport = new Vnet_ofport();
							add_op1.ofport_status = "wait";
							add_op1.ofport_id = "ofport~"+vnet_counter_ofport+"~"+id_tmp[2]+"~"+id_tmp[3];
							vnet_counter_ofport++;
							add_op1.ofport_portnum = n1;
							vnet_ofports.addItem(add_op1);
							add_l.link_ofport_src = add_op1.ofport_id;
							
							//add switch_ofport
							var add_swi_op1:Vnet_switch_ofport = new Vnet_switch_ofport();
							add_swi_op1.switch_id = add_l.link_src_id;
							add_swi_op1.ofport_id = add_op1.ofport_id;
							vnet_switch_ofports.addItem(add_swi_op1);
							tmp_swi_ops.addItem(add_swi_op1);
						}
						else {
							//add ofport
							var n2:int = 0;
							for(var s_op_num2:int=0;s_op_num2<tmp_swi_ops.length;s_op_num2++){
								if(tmp_swi_ops[s_op_num2].switch_id == add_l.link_src_id){
									for(var ofport1:int=0; ofport1<vnet_ofports.length; ofport1++){
										if(tmp_swi_ops[s_op_num2].ofport_id == vnet_ofports[ofport1].ofport_id){
											if(n2 < vnet_ofports[ofport1].ofport_portnum){
												n2 = vnet_ofports[ofport1].ofport_portnum;
												break;
											}
										}
									}
								}
							}
							var add_op2:Vnet_ofport = new Vnet_ofport();
							add_op2.ofport_status = "wait";
							add_op2.ofport_id = "ofport~"+vnet_counter_ofport+"~"+id_tmp[2]+"~"+id_tmp[3];
							vnet_counter_ofport++;
							add_op2.ofport_portnum = n2+1;
							vnet_ofports.addItem(add_op2);
							add_l.link_ofport_src = add_op2.ofport_id;
							
							//add switch_ofport
							var add_swi_op2:Vnet_switch_ofport = new Vnet_switch_ofport();
							add_swi_op2.switch_id = add_l.link_src_id;
							add_swi_op2.ofport_id = add_op2.ofport_id;
							vnet_switch_ofports.addItem(add_swi_op2);
							tmp_swi_ops.addItem(add_swi_op2);
						}
					}
					else if(vnet_updatelinks[vl_num10].fromObj.className == "Host"){
						add_l.link_src_id = Host(vnet_updatelinks[vl_num10].fromObj).getHost_ID();
						add_l.link_src_type = "Host";
					}
					if(vnet_updatelinks[vl_num10].toObj.className == "Switch"){
						add_l.link_dst_id = Switch(vnet_updatelinks[vl_num10].toObj).getSwitch_id();
						add_l.link_dst_type = "Switch";
						var swi_isnew2:Boolean = false;
						for(var s_num2:int=0; s_num2<vnet_add_swis.length; s_num2++){
							if(vnet_add_swis[s_num2].switch_id == add_l.link_dst_id){
								swi_isnew2 = true;
							}
						}
						if(swi_isnew2) {
							//add ofport
							var n3:int = 1;
							for(var s_op_num3:int=0;s_op_num3<tmp_swi_ops.length;s_op_num3++){
								if(tmp_swi_ops[s_op_num3].switch_id == add_l.link_dst_id){
									n3++;
								}
							}
							var add_op3:Vnet_ofport = new Vnet_ofport();
							add_op3.ofport_status = "wait";
							add_op3.ofport_id = "ofport~"+vnet_counter_ofport+"~"+id_tmp[2]+"~"+id_tmp[3];
							vnet_counter_ofport++;
							add_op3.ofport_portnum = n3;
							vnet_ofports.addItem(add_op3);
							add_l.link_ofport_dst = add_op3.ofport_id;
							
							//add switch_ofport
							var add_swi_op3:Vnet_switch_ofport = new Vnet_switch_ofport();
							add_swi_op3.switch_id = add_l.link_dst_id;
							add_swi_op3.ofport_id = add_op3.ofport_id;
							vnet_switch_ofports.addItem(add_swi_op3);
							tmp_swi_ops.addItem(add_swi_op3);
						}
						else {
							//add ofport
							var n4:int = 0;
							for(var s_op_num4:int=0; s_op_num4<tmp_swi_ops.length; s_op_num4++){
								if(tmp_swi_ops[s_op_num4].switch_id == add_l.link_dst_id){
									for(var ofport2:int=0; ofport2<vnet_ofports.length; ofport2++){
										if(tmp_swi_ops[s_op_num4].ofport_id == vnet_ofports[ofport2].ofport_id){
											if(n4 < vnet_ofports[ofport2].ofport_portnum){
												n4 = vnet_ofports[ofport2].ofport_portnum;
												break;
											}
										}
									}
								}
							}
							var add_op4:Vnet_ofport = new Vnet_ofport();
							add_op4.ofport_status = "wait";
							add_op4.ofport_id = "ofport~"+vnet_counter_ofport+"~"+id_tmp[2]+"~"+id_tmp[3];
							vnet_counter_ofport++;
							add_op4.ofport_portnum = n4+1;
							vnet_ofports.addItem(add_op4);
							add_l.link_ofport_dst = add_op4.ofport_id;
							
							//add switch_ofport
							var add_swi_op4:Vnet_switch_ofport = new Vnet_switch_ofport();
							add_swi_op4.switch_id = add_l.link_dst_id;
							add_swi_op4.ofport_id = add_op4.ofport_id;
							vnet_switch_ofports.addItem(add_swi_op4);
							tmp_swi_ops.addItem(add_swi_op4);
						}
					}
					else if(vnet_updatelinks[vl_num10].toObj.className == "Host"){
						add_l.link_dst_id = Host(vnet_updatelinks[vl_num10].toObj).getHost_ID();
						add_l.link_dst_type = "Host";
					}
					vnet_add_links.addItem(add_l);
					vnet_links.addItem(add_l);
					//add resource
					var v_res5:Vnet_vnet_resource = new Vnet_vnet_resource();
					v_res5.resource_id = add_l.link_id;
					v_res5.vnet_id = vnet_vnet.vnet_id;
					v_res5.resource_type = "link";
					v_res5.resource_status = "wait";
					var temp3:Array = v_res5.resource_id.split("~");
					v_res5.resource_timestamp = temp3[2];
					vnet_add_resources.addItem(v_res5);
					
					link_req = new Vnet_request("Add Virtual Link","9",vnet_vnet.vnet_id,vnet_updatelinks[vl_num10].link_id,executor_name + "~" +date.toString());
				}
			}
			
			else{ // vnet_updatelinks[vl_num10].status == "del"
				var id_tmp2:Array = vnet_updatelinks[vl_num10].link_id.split("~");
				
				if(id_tmp2[0] == "oflink"){
					link_req = new Vnet_request("Delete oflink","12",vnet_vnet.vnet_id,vnet_updatelinks[vl_num10].link_id,executor_name + "~" +date.toString());
					for(var oflink_num:int=0; oflink_num<vnet_oflinks.length; oflink_num++){
						if(vnet_oflinks[oflink_num].oflink_id == vnet_updatelinks[vl_num10].link_id){
							vnet_oflinks.removeItemAt(oflink_num);
							break;
						}
					}
				}
				else if(id_tmp2[0] == "link"){ //delete link
					for(var l_num1:int=0; l_num1<vnet_links.length; l_num1++){
						if(vnet_links[l_num1].link_id == vnet_updatelinks[vl_num10].link_id){
							if (vnet_links[l_num1].link_src_type == "Switch"){
								//delete ofport
								for(var v_op1:int=0; v_op1<vnet_ofports.length; v_op1++){
									if(vnet_ofports[v_op1].ofport_id == vnet_links[l_num1].link_ofport_src){
										vnet_ofports.removeItemAt(v_op1);
										break;
									}
								}
								//delete switch_ofport
								for(var s_op1:int=0; s_op1<vnet_switch_ofports.length; s_op1++){
									if(vnet_switch_ofports[s_op1].ofport_id == vnet_links[l_num1].link_ofport_src){
										vnet_switch_ofports.removeItemAt(s_op1);
										break;
									}
								}
							}
							if (vnet_links[l_num1].link_dst_type == "Switch"){
								//delete ofport
								for(var v_op2:int=0; v_op2<vnet_ofports.length; v_op2++){
									if(vnet_ofports[v_op2].ofport_id == vnet_links[l_num1].link_ofport_dst){
										vnet_ofports.removeItemAt(v_op2);
										break;
									}
								}
								//delete switch_ofport
								for(var s_op2:int=0; s_op2<vnet_switch_ofports.length; s_op2++){
									if(vnet_switch_ofports[s_op2].ofport_id == vnet_links[l_num1].link_ofport_dst){
										vnet_switch_ofports.removeItemAt(s_op2);
										break;
									}
								}
							}
							vnet_links.removeItemAt(l_num1);
							break;
						}
					}
					link_req = new Vnet_request("Delete Virtual Link","10",vnet_vnet.vnet_id,vnet_updatelinks[vl_num10].link_id,executor_name + "~" +date.toString());
				}
			}
			vnet_requests.addItem(link_req);
		}
	}
	
	Vnet_FlexToJavaService.FlexToJava(vnet_ofports,vnet_add_cons,vnet_add_swis,vnet_add_hosts,vnet_add_oflinks,
									  vnet_add_links,vnet_switch_ofports,myvnet,tmp_executor_vnet,vnet_add_resources,
									  vnet_requests,vnet_add_instances,vnet_add_ins_flavor,vnet_add_ins_image,
									  vnet_add_ins_con,vnet_add_ins_host,tmplist,update_vnet_id);
	
	vnet_add_cons.removeAll();
	vnet_add_swis.removeAll();
	vnet_add_hosts.removeAll();
	vnet_add_oflinks.removeAll();
	vnet_add_links.removeAll();
	vnet_updatelinks.removeAll();
	vnet_add_resources.removeAll();
	vnet_add_instances.removeAll();
	vnet_add_ins_flavor.removeAll();
	vnet_add_ins_image.removeAll();
	vnet_add_ins_con.removeAll();
	vnet_add_ins_host.removeAll();
	vnet_del_cons.removeAll();
	vnet_del_hosts.removeAll();
	vnet_del_swis.removeAll();
	vnet_requests.removeAll();
	
	var update_timer:Timer = new Timer(1000*8,3);
	update_timer.addEventListener(TimerEvent.TIMER,update_onTime);
	loading("images/loading.gif");
	update_timer.start();	

}

private function update_onTime(event:TimerEvent):void{
//	if(timer.currentCount==1){
//		if(!req_ok){
//			Alert.show("you have waited for 8 s");
//		}
//		
//	}
//	if(timer.currentCount==2){
//		if(!req_ok){
//			Alert.show("you have waited for 16 s");
//		}
//	}
//	if(timer.currentCount==3){
//		if(!req_ok){
//			Alert.show("you have waited for 24 s");
//		}
//	}
}