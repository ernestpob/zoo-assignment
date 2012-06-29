class Zoo:
	def __init__(self,name,location):
		self.name = name
		self.zoo_location = location

	def print_detail(self):
		print self.name,self.zoo_location
	
	def search(self,place):
		print place.zoo_location

accrazoo=Zoo('ACCRAzoo','achimota')
accrazoo.print_detail()
accrazoo.search(accrazoo)

class Infrustructure(Zoo):
	def __init__(self,zoo,buildtype,location):
		Zoo.__init__(self,zoo.name,zoo.zoo_location)
		self.buildtype= buildtype
		self.location = location
		self.zoo = zoo

	
	def search(self,place):
		print place.buildtype,'at',place.location,'in',place.name,'at',self.zoo.search(self.zoo)



cage = Infrustructure(accrazoo,'cages','north gate')
office = Infrustructure(accrazoo,'office flat','south gate')
#cage.search(cage)

class  Cages(Infrustructure):
	def __init__(self,infustructure,security_level,cage_no):
		Infrustructure.__init__(self,infustructure.zoo,infustructure.buildtype,infustructure.location)
		self.security_level= security_level
		self.cage_no = cage_no
		self.infustructure = infustructure
	
	
	def search(self,cage):
		print 'cage no.',cage.cage_no,'at',self.infustructure.search(cage)
	



class Offices(Infrustructure):
	def __init__(self,infustructure,Dept,room_no):
		Infrustructure.__init__(self,infustructure.zoo,infustructure.buildtype,infustructure.location)
		self.infustructure = infustructure
		self.Dept = Dept
		self.room_no = room_no

	def search(self,office):
		print 'Office is in room',office.room_no,'at',self.infustructure.search(office)

den = Cages(cage,'high',24)
den.search(den)

manager_office = Offices(office,'Administration','AD201')
manager_office.search(manager_office)
