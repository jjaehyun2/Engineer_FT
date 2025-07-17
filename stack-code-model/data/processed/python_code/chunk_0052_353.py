package dao
{
	import context.Context;
	
	import flash.data.SQLConnection;
	import flash.utils.ByteArray;
	
	import model.Employee;
	
	import mx.collections.ArrayCollection;
	import mx.utils.Base64Decoder;
	
	public class EmployeeDAO extends BaseDAO
	{
		public function EmployeeDAO()
		{
			sqlConnection = Context.getAttribute("sqlConnection"); 	
		}		
		
		public function getItem(id:String):Employee
		{
			return getSingleItem("SELECT id, firstName, lastName, title, department, city, email, phone, cellPhone, managerId, picture FROM employee WHERE id=?", id) as Employee;
		}

		public function findByManager(managerId:String):ArrayCollection
		{
			return getList("SELECT id, firstName, lastName, title, department, city, email, phone, cellPhone, managerId, picture FROM employee WHERE managerId=? ORDER BY lastName, firstName", [managerId]);
		}

		public function findByName(searchKey:String):ArrayCollection
		{
			return getList("SELECT id, firstName, lastName, title, department, city, email, phone, cellPhone, managerId, picture FROM employee WHERE firstName LIKE '%"+searchKey+"%' OR lastName LIKE '%"+searchKey+"%' OR firstName || ' ' || lastName LIKE '%"+searchKey+"%' ORDER BY lastName, firstName LIMIT 100");
		}

		override protected function processRow(o:Object):Object
		{
			var employee:Employee = new Employee();
			employee.id = o.id;
			employee.firstName = o.firstName == null ? "" : o.firstName;
			employee.lastName = o.lastName == null ? "" : o.lastName;
			employee.title = o.title == null ? "" : o.title;
			employee.department = o.department == null ? "" : o.department;
			employee.city = o.city == null ? "" : o.city;
			employee.email = o.email == null ? "" : o.email;
			employee.phone = o.phone == null ? "" : o.phone;
			employee.cellPhone = o.cellPhone == null ? "" : o.cellPhone;
			employee.picture = o.picture;

			if (o.managerId != null)
			{
				var manager:Employee = new Employee();
				manager.id = o.managerId;
				employee.manager = manager;
			}
	
			employee.loaded = true;
			return employee;
		}
		
	}
}