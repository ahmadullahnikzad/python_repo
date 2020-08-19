electri_charge=input()
spin=input()
if electri_charge == '1/2' and spin == '-1/3':
    print('Strange Quark')
elif electri_charge == '2/3' and spin == '1/2':
    print('Charm Quark')  
elif electri_charge == '-1' and spin == '1/2':
    print('Electron Lepton')
elif electri_charge == '0' and spin == '1/2':
    print('Neutrino Lepton')
elif electri_charge == '0' and spin == '1':
    print('Photo Boson')