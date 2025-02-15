class TestInput:
    valiadName = "Swapnil"

    invaliadName = ["swapnil", "swapnil123", "sw@pnil"]

    valiadMail = "abc.xyz@bl.co.in"

    invaliadMail = ["abc.xyzbl.co.in", "abc.xyz@.co.in", "ab.cxyz@bl.co.in"]

    valiadPhone = "91 2314569870"

    invaliadPhone = ["9 1236547890", "7896541230236", "91 897456@231"]

    valiadPassword = "Swapnil@1"

    invaliadPassword = ["Swapn@", "@swapnil", "abc"]

    validMailIds = ["abc@yahoo.com", "abc-100@yahoo.com",
                      "abc.100@yahoo.com", "abc111@abc.com", "abc-100@abc.net", "abc.100@abc.com.au", "abc@1.com",
                      "abc@gmail.com.com", "abc+100@gmail.com"]

    invalidMmailIds = ["abc@.com.my", "abc123@gmail.a", "abc123@.com",
                        "abc123@.com.com", ".abc@abc.com", "abc()*@gmail.com", "abc..2002@gmail.com", "abc.@gmail.com",
                        "abc@abc@gmail.com", "abc@gmail.com.1a", "abc@gmail.com.aa.au"]