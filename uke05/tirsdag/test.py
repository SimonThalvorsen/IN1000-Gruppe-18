def klipp_og_send3(eske, kvm):
    kvm -= 3
    eske.append("Ting")
    return kvm

kvm_stoff = 500
eske = []

while kvm_stoff >= 3:
    kvm_stoff = klipp_og_send3(eske, kvm_stoff)

print(len(eske))


