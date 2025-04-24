# open the file and read mode

file_read = open("penguins.txt")
print("File in read mode-")
print(file_read.read())
file_read.close()

# open the file in write mode
file_write = open("penguins.txt", "w")
# write in the file
file_write.write("File in the write mode-")
file_write.write("some dude with a border crisis on his face has beef with penguins somehow.")
file_write.close()

# open the file in append mode
file_append = open("penguins.txt")
#append in the file
file_append.write("\n File in append mode-")
file_append.write("some dude with a border crisis on his face has beef with penguins somehow.")
file_append.close()