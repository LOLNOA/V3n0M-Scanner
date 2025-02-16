from pathlib import Path

def cache_Check():
    global cachestatus
    my_file1 = Path("v3n0m-lfi.txt")
    my_file2 = Path("v3n0m-rce.txt")
    my_file3 = Path("v3n0m-xss.txt")
    my_file5 = Path("v3n0m-sqli.txt")
    my_file4 = Path("IPLogList.txt")
    if (
        my_file1.is_file()
        or my_file2.is_file()
        or my_file3.is_file()
        or my_file4.is_file()
        or my_file5.is_file()
    ):
        cachestatus = "contains some things"
    else:
        cachestatus = "empty"

def sql_list_counter():
    global sql_count
    try:
        f = open("v3n0m-sqli.txt", encoding="utf-8")
        l = [x for x in f.readlines() if x != "\n"]
        sql_count = len(l)
    except FileNotFoundError:
        sql_count = 0

def lfi_list_counter():
    global lfi_count
    try:
        f = open("v3n0m-lfi.txt", encoding="utf-8")
        l = [x for x in f.readlines() if x != "\n"]
        lfi_count = len(l)
    except FileNotFoundError:
        lfi_count = 0

def xss_list_counter():
    global xss_count
    try:
        f = open("v3n0m-xss.txt", encoding="utf-8")
        l = [x for x in f.readlines() if x != "\n"]
        xss_count = len(l)
    except FileNotFoundError:
        xss_count = 0

def misc_list_counter():
    global misc_count
    try:
        f = open("v3n0m-misc.txt", encoding="utf-8")
        l = [x for x in f.readlines() if x != "\n"]
        misc_count = len(l)
    except FileNotFoundError:
        misc_count = 0

def rce_list_counter():
    global rce_count
    try:
        f = open("v3n0m-rce.txt", encoding="utf-8")
        l = [x for x in f.readlines() if x != "\n"]
        rce_count = len(l)
    except FileNotFoundError:
        rce_count = 0

def logo():
    cache_Check()
    sql_list_counter()
    lfi_list_counter()
    rce_list_counter()
    xss_list_counter()
    misc_list_counter()
    print(
        B
        + """

                                                   :=*#%%@%%#+-:         :-=+****+=:.
         Venom <  4.3.5  >                      .+%@@@@@@%*==--=+#%#+- :**+--:...::=+#%*-
      Enhanced Dorking & Vuln Scans           :#@@@@@@@+.          :=*%#=.             -#%-
          Now with eleet banner "             +@@@@@@@@:     :**=+***+====*#=.            :%#.
                          ...........:---. #@@@@@@@@-     -@.-=::::-=--+=+#@*:            #%
                    :---:....::::.        =@@@@@@@@*      =%.+-#+++=:--:+=+%@@%-           %#
                -=+*+*#%@@@@@@@@@@@@@%%#*:%@@@@@@@=        %:%@@@@@@@#*=:--+#@@@%:         -@-
             -*#+==-:..       .:-=*#@@@@@:@@@@@@#           *@@@@@@@@@@@%+=-=*@@@@*         @*
            ::                       .-=*:%@@@@@             +@@-...:=*@@@@+--%@@@@@-       #%
                                          +@@@@*              -#        -%@@++:%@@@@@=      *%
           long live blackhats          .*:@@@@+               .+         -%@==*@@@@@@*     ##
        RIP NovaCygni / d4rkc4t        -@@%=@@@*                 =          +@#-+@@@@@@+    @+
      + everyone else at d4rkc0d3     .@@@@@*%@@.   :=.           :          .#*=-#@@@@@-  :@:
                                      *@@@@@@#*@#     =*-         :            @#==#@@@@@  +%
              .-=+*%@@@@@%#+=:        %@@@@@@@@+*%:    +@*        :-           :@-=:#@@@@- @-
           :+%#++=::-==*@@@@@@@#=.    +@@@@@@@@@@**+:   #@*       .+            #@---=@@@*=#
         -##+---:-=-::-::=*@@@@@@@*:   @@@@@@@@@@@@%#+-  .-=      .#            -@-+:+:@@#=.
       :#+=-::::..:-=--=:-:-+%@@@@@@#: :@@@@@@@@@@@@@@#*=.        .%          .#:@+.+:##@%
      =@=-:::-+*+==--=+==--:--*@@@@@@@*. *@@@@@@@@@@@@@@@#=:      .@         :%-=@ = *:@@%
     +#:::-+#+.         :=*=-:-=#@@@@@@@= .*@@@@@@@@@@@@@@%-=:    +=       .*#. #=  -.++@#
    -@=::+*-*              -++:-:=*@@@@@@%:  :=*#%@@@%#*=:   :+==%+.     :*#:  -#   :.==@=
    %#::=%--*                :+:-:-=#@@@@@@*.                    .#-: .=%*:   :%.    =:@@.
    @*===*--+=                 ==..:=+%@@@@@@=                    -=-:+-     :#      +-@*
    *@+*-#--:=+:             .=%@%.   .-%@@@@@@=             .-=*#==-::    .*+       *%@ 
    .@@%:#+-=--=+=::....::-*%@@@@@@=     .+%@@@@@*:  -==+****+-:    .:.::-:+.       :@@-
     :@@@#%*--------:--==*@@@@@@@@#-*.      .=*#@@@@*=-.             .=:-:+:       +@@=
      .%@@@@@%##****#%@@@@@@@@@@+.   +=            ...:==============-. =: -     -%@@:
        -%@@@@@@@@@@@@@@@@@@@*:       :*:                                :     -%@@%.
          :+#@@@@@@@@@@%#+=:            =#:                                :=*@@@@+
              .::-::.                     *#-                        :=+#%@@@@@@+
                                           :#@#=:             .:=*#@@@@@@@@@@#-
                                             :*@@@%#*+====+*%@@@@@@@@@@@@@#=
                 E O F                         -+#@@@@@@@@@@@@@@@@@@%*=:
                                                                                               \n"""
    )
