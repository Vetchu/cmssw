import ROOT
f = ROOT.TFile.Open("AOD.root")
f.Print()
f.pwd()
f.ls()
b=f.Get("Events")
b.ls()
print b.GetEntry(0)
print b.GetEntries()
#c=b.GetBranch("CTPPSDiamondDigiedmDetSetVector_ctppsDiamondRawToDigi_TimingDiamond_CTPPS")
c=b.GetListOfBranches()
print c
print "\n\nEntering D"
d=b.GetBranch("CTPPSDiamondDigiedmDetSetVector_ctppsDiamondRawToDigi_TimingDiamond_CTPPS.")
dd=d.GetListOfBranches()
for ddd in dd:
	print ddd

print "\n\nEntering E"
e=d.FindBranch("CTPPSDiamondDigiedmDetSetVector_ctppsDiamondRawToDigi_TimingDiamond_CTPPS.obj")
ee=e.GetListOfBranches()
print ee[0]
for eee in ee:
	print eee

print "\n\nEntering F"
print e.IsFolder()
print ee[0].IsFolder()
print ee[0].GetParentName()
f=e.FindBranch("CTPPSDiamondDigiedmDetSetVector_ctppsDiamondRawToDigi_TimingDiamond_CTPPS.obj._sets")
print f

#f=e.FindBranch(ee[0].GetFileName())
ff=f.GetListOfBranches()
for fff in ff:
	print fff

g=f.FindBranch("detId()")

for a in g:
	print a
#for i in range(b.GetEntries()):
#	event=b.GetEntry(i)
#	print event 
