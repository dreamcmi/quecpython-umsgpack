from usr import umsgpack

something = {
    "key":1,
    "key2":2,
    "some":[1,2,3]
}

d_data = umsgpack.dumps(something)
print("dumps:")
print(d_data)

l_data = umsgpack.loads(d_data)
print("loads:")
print(l_data)