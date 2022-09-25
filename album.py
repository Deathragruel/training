def make_album(title, artist_name, number_of_songs = None):
	album = {'Title': title.title(), 'Artist Name': artist_name.title()}
	if number_of_songs:
		album['Number of songs'] = number_of_songs
	return album
album_description = make_album('nevermind', 'nirvana', 13)
print(album_description)
album_description = make_album('the dark side of the moon', 'pink floyd')
print(album_description)
album_description = make_album('rumours', 'fleetwood mac')
print(album_description)

while True:
	print("\nEnter q if you want to quit the loop.")
	print("Please enter the name of your favorite album and it's artist's name: ")
	album_name = input("Album name: ")
	if album_name == 'q':
		break
	author = input("Artist name: ")
	if author == 'q':
		break
	album_description = make_album(album_name, author)
	print(album_description)