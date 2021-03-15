import os
print("#################################################################")
print("                          Select Menu - LVM                          ")
print("#################################################################")
print("\t\t\t")
while True:
    print("""
    1. Disk Partitions
    2. Physical Volume
    3. Create Volume Group
    4. Create Logical Volume
    5. Extend Logical Volume Size
    6. Reduce Logical Volume Size
    7. Check Physical Volume
    8. Check Volume Group
    9. Check Logical Volume
    10. Remove Physical Volume
    11. Remove Volume Group
    12. Remove Logical Volume
    13. Exit
    """)
print("Enter your choice : ", end="")
    choice=input()
if int(choice) == 1:
        os.system("fdisk -l")
    elif int(choice) == 2:
        print("Enter disk name")
        disk_name=input()
        os.system("pvcreate {}".format(disk_name))
    elif int(choice) == 3:
        print("Enter PV(s) name (space between them)")
        pv_name=input()
        print("Enter Volume Group")
        vg_name=input()
        os.system("vgcreate {0} {1}".format(vg_name, pv_name))
    elif int(choice) == 4:
        print("Is mount directory present already(Y/N)?")
        response=input()
        if response == 'Y':
            print("Enter mount directory with the path")
            directory=input()
            print("Enter Logical Volume")
            lv_name=input()
            print("Enter Volume Group")
            vg_name=input()
            print("Enter the LV size with units(K,M,G,T,P)")
            size=input()
            os.system("lvcreate --size {0} --name {1} {2}".format(size, lv_name, vg_name))
            os.system("mkfs.ext4 /dev/{0}/{1}".format(vg_name, lv_name))
            os.system("mount /dev/{0}/{1} {2}".format(vg_name, lv_name, directory))
            os.system("echo mount /dev/{0}/{1} {2} >> /etc/rc.d/rc.local".format(vg_name, lv_name, directory))
        elif response == 'N':
            print("Enter mount directory to be created with the path")
            directory=input()
            os.system("mkdir {}".format(directory))
            print("Enter Logical Volume")
            lv_name=input()
            print("Enter Volume Group")
            vg_name=input()
            print("Enter the LV size with units(K,M,G,T,P)")
            size=input()
            os.system("lvcreate --size {0} --name {1} {2}".format(size, lv_name, vg_name))
            os.system("mkfs.ext4 /dev/{0}/{1}".format(vg_name, lv_name))
            os.system("mount /dev/{0}/{1} {2}".format(vg_name, lv_name, directory))
            os.system("echo mount /dev/{0}/{1} {2} >> /etc/rc.d/rc.local".format(vg_name, lv_name, directory))
        else:
            print("Invalid Option")
    elif int(choice) == 5:
        print("Enter Logical Volume")
        lv_name=input()
        print("Enter Volume Group")
        vg_name=input()
        print("Enter the increse in size of LV with units(K,M,G,T,P)")
        size_increase=input()
        os.system("lvextend --size +{0} /dev/{1}/{2}".format(size_increase, vg_name, lv_name))
        os.system("resize2fs /dev/{0}/{1}".format(vg_name, lv_name))
    elif int(choice) == 6:
        print("Enter Logical Volume")
        lv_name=input()
        print("Enter Volume Group")
        vg_name=input()
        print("Enter mounted directory with the path")
        directory=input()
        print("Enter the decrese in LV size with units(K,M,G,T,P)")
        size_decrease=input()
        os.system("umount {}".format(directory))
        os.system("e2fsck -f /dev/mapper/{0}-{1}".format(vg_name, lv_name))
        os.system("resize2fs /dev/mapper/{0}-{1}  {2}".format(vg_name, lv_name, size_decrease))
        os.system("echo Y | lvreduce -L {0}  /dev/mapper/{1}-{2} ".format(size_decrease, vg_name, lv_name))
        os.system("e2fsck -f /dev/mapper/{0}-{1}".format(vg_name, lv_name))
        os.system("mount /dev/{0}/{1} {2}".format(vg_name, lv_name, directory))
    elif int(choice) == 7:
        print("Enter Physical Volume")
        pv_name=input()
        os.system("pvdisplay {}".format(pv_name))
    elif int(choice) == 8:
        print("Enter Volume Group")
        vg_name=input()
        os.system("vgdisplay {}".format(vg_name))
    elif int(choice) == 9:
        print("Enter Logical Volume")
        lv_name=input()
        print("Enter Volume Group")
        vg_name=input()
        os.system("lvdisplay /dev/{0}/{1}".format(vg_name, lv_name))
    elif int(choice) == 10:
        print("Enter Physical Volume(s)(space between them) to be removed")
        pv_name=input()
        os.system("pvremove {}".format(pv_name))
    elif int(choice) == 11:
        print("Enter Volume Group to be removed")
        vg_name=input()
        os.system("vgchange -an {}".format(vg_name))
        os.system("vgremove {}".format(vg_name))
    elif int(choice) == 12:
        print("Enter Volume Group")
        vg_name=input()
        print("Enter Logical Volume to be removed")
        lv_name=input()
        print("Enter mounted directory with the path")
        directory=input()
        os.system("umount {}".format(directory))
        os.system("lvchange -an /dev/{0}/{1}".format(vg_name, lv_name))
        os.system("lvremove /dev/{0}/{1}".format(vg_name, lv_name))
    elif int(choice) == 13:
        exit()
    else:
        print("Option not supported")
    input("Enter to continue...")
    os.system("clear")
