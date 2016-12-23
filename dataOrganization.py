import csv
import pandas as pd



def MakeWeka(movie_num):
	col_list = movie_num.columns
	col_list_type = {}
	for col in col_list:
		col_list_type[col] = 'numeric'
	# print col_list_type

	foo = open('train.arff', 'w+')
	foo.write('@relation movieGross\n\n')
	for col in col_list:
		if(col != 'gross'):
			if(col != col_list[-1]):
				foo.write('@attribute ' + col + ' ' + col_list_type[col] + '\n')
			else:
				foo.write('@attribute ' + col + ' ' + col_list_type[col] + '\n')
				foo.write('@attribute gross ' + col_list_type[col] + '\n')

	foo.write('\n@data\n')
	for index, row in movie_num.iterrows():
		for col in col_list:

			if (col != 'gross'):
				foo.write(str(row[col]))

			if(col != col_list[-1]):
				if (col != 'gross'):
					foo.write(',')
			else:
				foo.write(',' + str(row['gross']) + '\n')
	foo.close()

	return 0


def main():
	movie = pd.read_csv('mov_mm_train.csv') ### reads the csv and creates the dataframe called movie
	#print movie.head()
	str_list = [] ### empty list to contain columns with strings (words)
	for colname, colvalue in movie.iteritems():
	    if type(colvalue[1]) == str:
	        str_list.append(colname)

	### Get to the numeric columns by inversion            
	num_list = movie.columns.difference(str_list)
	#print num_list
	movie_num = movie[num_list]

	# movie_num = movie_num.dropna(subset=['gross','num_critic_for_reviews','num_user_for_reviews','num_voted_users','movie_facebook_likes'])
	movie_num = movie_num.dropna()
	for col in movie_num:
		if(col != 'gross'):
			movie_num[col] = (movie_num[col] - movie_num[col].mean()) / (movie_num[col].max() - movie_num[col].min())
		
	MakeWeka(movie_num)


if __name__ == '__main__':
    main()