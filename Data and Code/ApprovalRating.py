import MySQLdb as db;

con = db.connect('localhost', 'root', '', 'test');

cursor = con.cursor();

date = 2;

while date <= 29:
	if date < 10:
		if (date+6) < 10:
			totalRowsq = "SELECT count(*) FROM result where stTime BETWEEN '"+ str(date) +"-11-2017 00:00:00' AND '"+ str(date+6) +"-11-2017 23:59:59';"
			weightedQuery = "SELECT count(*) FROM result where stTime BETWEEN '"+ str(date) +"-11-2017 00:00:00' AND '"+ str(date+6) +"-11-2017 23:59:59' and mScore > 0;"
			affinQuery = "SELECT count(*) FROM result where stTime BETWEEN '"+ str(date) +"-11-2017 00:00:00' AND '"+ str(date+6) +"-11-2017 23:59:59' and aScore > 0;"
			SentiWordQuery = "SELECT count(*) FROM result where stTime BETWEEN '"+ str(date) +"-11-2017 00:00:00' AND '"+ str(date+6) +"-11-2017 23:59:59' and sScore > 0;"
		else:
			totalRowsq = "SELECT count(*) FROM result where stTime BETWEEN '"+ str(date) +"-11-2017 00:00:00' AND '"+ str(date+6) +"-11-2017 23:59:59';"
			weightedQuery = "SELECT count(*) FROM result where stTime BETWEEN '"+ str(date) +"-11-2017 00:00:00' AND '"+ str(date+6) +"-11-2017 23:59:59' and mScore > 0;"
			affinQuery = "SELECT count(*) FROM result where stTime BETWEEN '"+ str(date) +"-11-2017 00:00:00' AND '"+ str(date+6) +"-11-2017 23:59:59' and aScore > 0;"
			SentiWordQuery = "SELECT count(*) FROM result where stTime BETWEEN '"+ str(date) +"-11-2017 00:00:00' AND '"+ str(date+6) +"-11-2017 23:59:59' and sScore > 0;"
	else:
		totalRowsq = "SELECT count(*) FROM result where stTime BETWEEN '"+ str(date) +"-11-2017 00:00:00' AND '"+ str(date+6) +"-11-2017 23:59:59';"	
		weightedQuery = "SELECT count(*) FROM result where stTime BETWEEN '"+ str(date) +"-11-2017 00:00:00' AND '"+ str(date+6) +"-11-2017 23:59:59' and mScore > 0;"
		affinQuery = "SELECT count(*) FROM result where stTime BETWEEN '"+ str(date) +"-11-2017 00:00:00' AND '"+ str(date+6) +"-11-2017 23:59:59' and aScore > 0;"
		SentiWordQuery = "SELECT count(*) FROM result where stTime BETWEEN '"+ str(date) +"-11-2017 00:00:00' AND '"+ str(date+6) +"-11-2017 23:59:59' and sScore > 0;"

	cursor.execute(totalRowsq);
	
	totalrows = 0;
	positiverows = 0;
	positiverowsaffinonly = 0;
	positiverowsSentiWordnet = 0;
	
	for row in cursor:
		totalrows = row[0];
	
	cursor.execute(weightedQuery);
	
	for row in cursor:
		positiverows = row[0];
	
	approvalrating = 0;
	if totalrows != 0:	
		approvalrating = format((positiverows / totalrows) * 100,'.2f');
	
	cursor.execute(affinQuery);
	
	for row in cursor:
		positiverowsaffinonly = row[0];
		
	approvalratingaffinonly = 0;
	if totalrows != 0:
		approvalratingaffinonly = format((positiverowsaffinonly / totalrows) * 100,'.2f');
		
	cursor.execute(SentiWordQuery);
	
	for row in cursor:
		positiverowsSentiWordnet = row[0];
		
	approvalratingSentiWordnetonly = 0;
	if totalrows != 0:
		approvalratingSentiWordnetonly = format((positiverowsSentiWordnet / totalrows) * 100,'.2f');
	
	print("Weekly Approval Rating between " + str(date)+"-11-2017 and "+ str(date+6) +"-11-2017 (affin) : " + str(approvalratingaffinonly) + "%");
	print("Weekly Approval Rating between " + str(date)+"-11-2017 and "+ str(date+6) +"-11-2017 (SentiWordNet): " + str(approvalratingSentiWordnetonly) + "%");
	print("Weekly Approval Rating between " + str(date)+"-11-2017 and "+ str(date+6) +"-11-2017 (weighted): " + str(approvalrating) + "%");
	date = date + 7;

date = 22;

while date <= 30:
	if date < 10:
		queryDaily = "SELECT count(*) FROM result where stTime BETWEEN '0"+ str(date) +"-11-2017 00:00:00' AND '0"+ str(date) +"-11-2017 23:59:59';"
		weightedDaily = "SELECT count(*) FROM result where stTime BETWEEN '0"+ str(date) +"-11-2017 00:00:00' AND '0"+ str(date) +"-11-2017 23:59:59' and mScore > 0;"
		affinQueryDaily = "SELECT count(*) FROM result where stTime BETWEEN ''0"+ str(date) +"-11-2017 00:00:00' AND '0"+ str(date) +"-11-2017 23:59:59' and aScore > 0;"
		SentiWordQuery = "SELECT count(*) FROM result where stTime BETWEEN ''0"+ str(date) +"-11-2017 00:00:00' AND '0"+ str(date) +"-11-2017 23:59:59' and sScore > 0;"
	else:
		queryDaily = "SELECT count(*) FROM result where stTime BETWEEN '"+ str(date) +"-11-2017 00:00:00' AND '"+ str(date) +"-11-2017 23:59:59';"	
		weightedDaily = "SELECT count(*) FROM result where stTime BETWEEN '"+ str(date) +"-11-2017 00:00:00' AND '"+ str(date) +"-11-2017 23:59:59' and mScore > 0;"
		affinQueryDaily = "SELECT count(*) FROM result where stTime BETWEEN '"+ str(date) +"-11-2017 00:00:00' AND '"+ str(date) +"-11-2017 23:59:59' and aScore > 0;"
		SentiWordQuery = "SELECT count(*) FROM result where stTime BETWEEN '"+ str(date) +"-11-2017 00:00:00' AND '"+ str(date) +"-11-2017 23:59:59' and sScore > 0;"
	
	cursor.execute(queryDaily);
	
	totalrows = 0;
	positiverows = 0;
	positiverowsaffinonly = 0;
	positiverowsSentiWordnetonly=0;
	
	totalrows = cursor.fetchone()[0];
	
	cursor.execute(weightedDaily);
	
	
	for row in cursor:
		positiverows = row[0];
	
	approvalratingDaily = 0;
	if totalrows != 0:	
		approvalratingDaily = format((positiverows / totalrows) * 100,'.2f');
	
	cursor.execute(affinQueryDaily);
	
	for row in cursor:
		positiverowsaffinonly = row[0];
	
	approvalratingaffinonlyDaily = 0;
	if totalrows != 0:
		approvalratingaffinonlyDaily = format((positiverowsaffinonly / totalrows) * 100,'.2f');
		
	cursor.execute(SentiWordQuery);
	
	for row in cursor:
		positiverowsSentiWordnetonly = row[0];
		
	approvalratingSentiWordnetDaily = 0;
	if totalrows != 0:
		approvalratingSentiWordnetDaily = format((positiverowsSentiWordnetonly / totalrows) * 100,'.2f');
	
	print("Daily Approval Rating on " + str(date)+"-11-2017 (affin): " + str(approvalratingaffinonlyDaily) + "%");
	print("Daily Approval Rating on " + str(date)+"-11-2017 (sentiWordNet): " + str(approvalratingSentiWordnetDaily) + "%");
	print("Daily Approval Rating on " + str(date)+"-11-2017 (weighted): " + str(approvalratingDaily) + "%");
	date = date + 1;