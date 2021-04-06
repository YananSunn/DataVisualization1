name_list =['Wii','NES','GB','DS','X360','PS3','PS2','SNES','GBA','3DS','PS4','N64','PS','XB','PC','2600','PSP','XOne','GC','WiiU','GEN','DC','PSV','SAT','SCD','WS','NG','TG16','3DO','GG','PCFX']
color_list =[]

print("var colors = {")
for i in range(0,len(name_list)):
	print("    '"+name_list[i]+"':\"#"+color_list[i]+'",')
print("};")