variables = {}

def AND(*args):
	clause = []
	for arg in args:
		if isinstance(arg, list):
			clause.push(arg)
		else:
			return "Invalid CNF format"
	return clause

def OR(*args):
	cluase=[]
	for arg in args:
		if isinstance(arg, int):
			clause.push(arg)
		else:
			if isinstance(arg, basestring):
				if not arg in variables:
					variables[arg] = len(variables)
				clause.push(variables[arg])
			else:
				return "Invalid CNF format"
	return clause

def NOT(variable):
	if isinstance(variable, basestring):
		if not variable in variables:
			variables[variable] = len(variables)
		return variables[variable]
	else:
		return "Invalid CNF format"


