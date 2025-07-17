class characters.Person
{
   static var idCount = 0;
   var id = 1;
   function Person(gender, curAge, isSpouse)
   {
      this.id = characters.Person.idCount;
      characters.Person.idCount = characters.Person.idCount + 1;
      this.male = gender;
      this.age = curAge;
      this.health = 100;
      this.pregnant = false;
      this.spouse = isSpouse;
      this.marriedTo = -1;
      this.educationLvl = 5;
      this.headOfFamily = false;
      if(gender && this.age > 20 && !isSpouse)
      {
         this.headOfFamily = false;
      }
      this.workEfficiency = 10000000;
      this.fertile = true;
      if(this.age < 1)
      {
         this.fertile = true;
      }
      this.atSchool = false;
      this.firstName = "";
      this.calculateWorkEfficiency();
      this.createName(this.male);
      this.findSprite();
   }
   function init()
   {
      this.createName(this.male);
      this.findSprite();
   }
   function getAtSchool()
   {
      return this.atSchool;
   }
   function setAtSchool(a)
   {
      this.atSchool = a;
   }
   function getFertile()
   {
      return this.fertile;
   }
   function setFertile(f)
   {
      this.fertile = f;
   }
   function getHeadOfFamily()
   {
      return this.headOfFamily;
   }
   function setHeadOfFamily(h)
   {
      this.headOfFamily = h;
   }
   function getWorkEfficiency()
   {
      return this.workEfficiency;
   }
   function setWorkEfficiency(w)
   {
      this.workEfficiency = w;
   }
   function getGender()
   {
      return this.male;
   }
   function getName()
   {
      return this.firstName;
   }
   function setName(newname)
   {
      this.firstName = newname;
   }
   function getAge()
   {
      return this.age;
   }
   function setAge(age)
   {
      this.age = age;
   }
   function getID()
   {
      return this.id;
   }
   function getHealth()
   {
      return this.health;
   }
   function setHealth(health)
   {
      this.health = health;
   }
   function getSpouse()
   {
      return this.spouse;
   }
   function setSpouse(is)
   {
      this.spouse = is;
   }
   function getEducationLvl()
   {
      return this.educationLvl;
   }
   function increaseEducationLvl()
   {
      this.educationLvl = this.educationLvl + 1;
   }
   function setPregnant(is)
   {
      this.pregnant = is;
   }
   function getPregnant()
   {
      return this.pregnant;
   }
   function setMarriedTo(index)
   {
      this.marriedTo = index;
   }
   function getMarriedTo()
   {
      return this.marriedTo;
   }
   function paint(xpos, id)
   {
      var _loc3_ = _root.familyMemberTarget.attachMovie(this.image,this.image,id * 50);
      _loc3_._x = xpos;
      if(this.image == "familyMember1")
      {
         _loc3_._y = 0;
      }
      else if(this.image == "familyMember2")
      {
         _loc3_._y = 0;
      }
      else
      {
         _loc3_._y = -16;
      }
      _loc3_._name = "person" + id;
      _loc3_.hitArea = _loc3_.hitArea;
      _loc3_.onRelease = function()
      {
         _root.arrangeFamilyMemberInfoBox(this.getDepth() / 50);
      };
   }
   function findSprite()
   {
      var _loc2_ = undefined;
      if(this.male && this.age > 15)
      {
         _loc2_ = 1;
      }
      else if(this.male)
      {
         _loc2_ = 3;
      }
      else if(this.age > 15)
      {
         _loc2_ = 2;
      }
      else
      {
         _loc2_ = 4;
      }
      this.image = "familyMember" + _loc2_;
      return this.image;
   }
   function calculateWorkEfficiency()
   {
      var _loc3_ = 0;
      if(this.age == 0)
      {
         _loc3_ = -20;
      }
      else if(this.age == 1)
      {
         _loc3_ = -10;
      }
      else if(this.age < 5)
      {
         _loc3_ = 0;
      }
      else if(this.age < 16)
      {
         _loc3_ = 50;
      }
      else if(this.age < 50)
      {
         _loc3_ = 100;
      }
      else
      {
         _loc3_ = 80;
      }
      _loc3_ = _loc3_ + this.educationLvl * 5;
      if(_loc3_ > 0)
      {
         _loc3_ = _loc3_ * this.health / 100;
      }
      if(this.pregnant && _loc3_ > 0)
      {
         _loc3_ = _loc3_ / 2;
      }
      if(this.atSchool && _loc3_ > 0)
      {
         _loc3_ = _loc3_ / 2;
         if(!_root.schoolBuilt)
         {
            _loc3_ = _loc3_ / 2;
         }
      }
      _loc3_ = Math.round(_loc3_);
      _loc3_ = Math.round(_loc3_ * 0.75);
      this.setWorkEfficiency(_loc3_);
   }
   function createName(gender)
   {
      var _loc3_ = Math.round(random(12)) + 1;
      var _loc2_ = undefined;
      if(gender)
      {
         switch(_loc3_)
         {
            case 1:
               _loc2_ = "fiannly done";
               break;
            case 2:
               _loc2_ = "of any original names";
               break;
            case 3:
               _loc2_ = "i cant think";
               break;
            case 4:
               _loc2_ = "bitch cock sucker";
               break;
            case 5:
               _loc2_ = "oh nigger";
               break;
            case 6:
               _loc2_ = "lesbian";
               break;
            case 7:
               _loc2_ = "gay";
               break;
            case 8:
               _loc2_ = "cancer";
               break;
            case 9:
               _loc2_ = "penises";
               break;
            case 10:
               _loc2_ = "fortnite";
               break;
            case 11:
               _loc2_ = "tracer";
               break;
            case 12:
               _loc2_ = "Lisimba";
         }
      }
      else
      {
         switch(_loc3_)
         {
            case 1:
               _loc2_ = "nigger";
               break;
            case 2:
               _loc2_ = "faggot";
               break;
            case 3:
               _loc2_ = "chinese";
               break;
            case 4:
               _loc2_ = "kill me";
               break;
            case 5:
               _loc2_ = "rape me";
               break;
            case 6:
               _loc2_ = "fertile";
               break;
            case 7:
               _loc2_ = "well fuck";
               break;
            case 8:
               _loc2_ = "i have a long ass name";
               break;
            case 9:
               _loc2_ = "shit cunt";
               break;
            case 10:
               _loc2_ = "fuck";
               break;
            case 11:
               _loc2_ = "death";
               break;
            case 12:
               _loc2_ = "lol";
         }
      }
      this.firstName = _loc2_;
   }
}