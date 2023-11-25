students = {
	"Prasad" : "A",
	"shrikant" : "B",
	"sai" : "c"
}

for student in students:
	print(student,students[student],sep=", ")


# dic inside a list

students = [{"name": "Herminoe", "House" : "gryffindor", "patronus" : "outter"}, 
{"name": "Harry", "House" : "gryffindor", "patronus" : "stage"}, 
{"name": "Ron", "House" : "gryffindor", "patronus" : "Jack"},
{"name": "Draco", "House" : "Slytherin", "patronus" : None}]

for student in students:
	print(student["name"],student["House"],student["patronus"],sep=", ")