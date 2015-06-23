class CNF:
	def __init__(self):
		self.variables = {"empty":0}

	def AND(self, *args):
		clause = []
		for arg in args:
			if isinstance(arg, list):
				clause.append(arg)
			else:
				return "Invalid CNF format"
		return clause

	def OR(self, *args):
		clause=[]
		for arg in args:
			if isinstance(arg, int):
				clause.append(arg)
			else:
				if isinstance(arg, basestring):
					if not arg in self.variables:
						self.variables[arg] = len(self.variables)
					clause.append(self.variables[arg])
				else:
					return "Invalid CNF format"
		return clause

	def NOT(self,variable):
		if isinstance(variable, basestring):
			if not variable in self.variables:
				self.variables[variable] = len(self.variables)
			return -self.variables[variable]
		else:
			return "Invalid CNF format"

	def NUMBER_OF_VARIABLES(self):
		return len(self.variables)

	def getVariables(self):
		return self.variables

	def WRITE(self, clause):
		listOfVars = []
		for var in clause:
			if var < 0: 
				lvalue = -var
			else:
				lvalue = var

			lKey = [key for key, value in self.variables.iteritems() if value == lvalue][0]
			if var < 0:
				lKey = "NOT "+lKey;
			listOfVars.append(lKey)
		print listOfVars

