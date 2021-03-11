import munch

sample = {
    "a":1,
    "b":"c"
}

a = munch.munchify(sample)

print(munch.unmunchify(a))