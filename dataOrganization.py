import csv
import pandas as pd



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
	print len(movie_num)

if __name__ == '__main__':
    main()