width = 25
height = 6
laylength = width*height
data = ""

with open("./input", "r") as f:
    data = f.readline().strip()

#data = "0222112222120000"
    
layers = {}

i = 0
while i*laylength < len(data):
    layers[i] = data[i*laylength:i*laylength+laylength]
    #print(layers[i])
    i += 1

result = []
for i in range(0, laylength):
    for y in range(0, len(layers)):
        if layers[y][i] != '2':
            result.append(layers[y][i])
            break

print(len(result))
print(result)
i=0
s = []
#while i*width < len(result):
s = "".join(map(str, result))#i*width:i*width+width])))
i += 1

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

#for i in range(0, len(s)):
#    print(int(s[i], 2))
#n = int(s, 2)
#l = n.to_bytes((n.bit_length() + 7) //8, 'big').decode()

print(text_from_bits(s))
