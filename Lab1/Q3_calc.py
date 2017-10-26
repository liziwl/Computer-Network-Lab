def ans(distant_km, trans_rate_in_G , speed, package_length):
    bits = distant_km*1000 / speed * trans_rate_in_G *1e9
    # 1.
    if package_length <= bits:
        print("Ans1: %d bits in the link in maximum." %package_length)
    else:
        print("Ans1: %d bits in the link in maximum." %bits)
    # 2.
    print("Ans2: The width of a bit is %.3f m in the link." %(distant_km*1000/bits))
    # 3.
    print("Ans3: Using %.3f s." % (distant_km * 1000 / speed + package_length / (trans_rate_in_G*1e9)))
ans(50000, 2, 2e8, 1024)