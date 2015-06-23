import pycosat
import buildClauses as cl

def SAT(clause):
	return list(pycosat.itersolve(clause))


def WRITE_SAT_SOLUTIONS(icnf,solutions):
	for sol in solutions:
		icnf.WRITE(sol)

def countTrueVariables(solution):
	count = 0
	for var in solution:
		if var>0:
			count += 1
	return count


def STINGYSAT(clause, k):
	return "Solution for STINGYSAT"

def reduceSatToStingySAT(cnf, clause):
	return STINGYSAT(clause, cnf.NUMBER_OF_VARIABLES())

def reduceStingySatToSAT(clause, k):
	solutions = SAT(clause)
	for solution in solutions:
		if k == countTrueVariables(solution):
			return "TRUE"
	return "FALSE"




if __name__ == '__main__':
	cnf = cl.CNF()
	newClause = cnf.AND(cnf.OR("A",cnf.NOT("E"),"D"),cnf.OR(cnf.NOT("A"),"E","C","D"),cnf.OR(cnf.NOT("C"),cnf.NOT("D")))
	print reduceStingySatToSAT(newClause, 2)