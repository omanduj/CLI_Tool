from CLI_Combos import __version__
from CLI_Combos.logic import get_pins


def test_version():
    assert __version__ == "0.1.0"


def test_pins():
    assert get_pins("1234") == {
        "1121",
        "1124",
        "1125",
        "1127",
        "1131",
        "1134",
        "1135",
        "1137",
        "1161",
        "1164",
        "1165",
        "1167",
        "1221",
        "1224",
        "1225",
        "1227",
        "1231",
        "1234",
        "1235",
        "1237",
        "1261",
        "1264",
        "1265",
        "1267",
        "1321",
        "1324",
        "1325",
        "1327",
        "1331",
        "1334",
        "1335",
        "1337",
        "1361",
        "1364",
        "1365",
        "1367",
        "1521",
        "1524",
        "1525",
        "1527",
        "1531",
        "1534",
        "1535",
        "1537",
        "1561",
        "1564",
        "1565",
        "1567",
        "2121",
        "2124",
        "2125",
        "2127",
        "2131",
        "2134",
        "2135",
        "2137",
        "2161",
        "2164",
        "2165",
        "2167",
        "2221",
        "2224",
        "2225",
        "2227",
        "2231",
        "2234",
        "2235",
        "2237",
        "2261",
        "2264",
        "2265",
        "2267",
        "2321",
        "2324",
        "2325",
        "2327",
        "2331",
        "2334",
        "2335",
        "2337",
        "2361",
        "2364",
        "2365",
        "2367",
        "2521",
        "2524",
        "2525",
        "2527",
        "2531",
        "2534",
        "2535",
        "2537",
        "2561",
        "2564",
        "2565",
        "2567",
        "4121",
        "4124",
        "4125",
        "4127",
        "4131",
        "4134",
        "4135",
        "4137",
        "4161",
        "4164",
        "4165",
        "4167",
        "4221",
        "4224",
        "4225",
        "4227",
        "4231",
        "4234",
        "4235",
        "4237",
        "4261",
        "4264",
        "4265",
        "4267",
        "4321",
        "4324",
        "4325",
        "4327",
        "4331",
        "4334",
        "4335",
        "4337",
        "4361",
        "4364",
        "4365",
        "4367",
        "4521",
        "4524",
        "4525",
        "4527",
        "4531",
        "4534",
        "4535",
        "4537",
        "4561",
        "4564",
        "4565",
        "4567",
    }

    assert get_pins("0230") == {
        "0120",
        "0128",
        "0130",
        "0138",
        "0160",
        "0168",
        "0220",
        "0228",
        "0230",
        "0238",
        "0260",
        "0268",
        "0320",
        "0328",
        "0330",
        "0338",
        "0360",
        "0368",
        "0520",
        "0528",
        "0530",
        "0538",
        "0560",
        "0568",
        "8120",
        "8128",
        "8130",
        "8138",
        "8160",
        "8168",
        "8220",
        "8228",
        "8230",
        "8238",
        "8260",
        "8268",
        "8320",
        "8328",
        "8330",
        "8338",
        "8360",
        "8368",
        "8520",
        "8528",
        "8530",
        "8538",
        "8560",
        "8568",
    }

    assert get_pins("0000") == {
        "0000",
        "0008",
        "0080",
        "0088",
        "0800",
        "0808",
        "0880",
        "0888",
        "8000",
        "8008",
        "8080",
        "8088",
        "8800",
        "8808",
        "8880",
        "8888",
    }

    assert get_pins("1111") == {
        "1111",
        "1112",
        "1114",
        "1121",
        "1122",
        "1124",
        "1141",
        "1142",
        "1144",
        "1211",
        "1212",
        "1214",
        "1221",
        "1222",
        "1224",
        "1241",
        "1242",
        "1244",
        "1411",
        "1412",
        "1414",
        "1421",
        "1422",
        "1424",
        "1441",
        "1442",
        "1444",
        "2111",
        "2112",
        "2114",
        "2121",
        "2122",
        "2124",
        "2141",
        "2142",
        "2144",
        "2211",
        "2212",
        "2214",
        "2221",
        "2222",
        "2224",
        "2241",
        "2242",
        "2244",
        "2411",
        "2412",
        "2414",
        "2421",
        "2422",
        "2424",
        "2441",
        "2442",
        "2444",
        "4111",
        "4112",
        "4114",
        "4121",
        "4122",
        "4124",
        "4141",
        "4142",
        "4144",
        "4211",
        "4212",
        "4214",
        "4221",
        "4222",
        "4224",
        "4241",
        "4242",
        "4244",
        "4411",
        "4412",
        "4414",
        "4421",
        "4422",
        "4424",
        "4441",
        "4442",
        "4444",
    }

    assert get_pins("0909") == {
        "0606",
        "0608",
        "0609",
        "0686",
        "0688",
        "0689",
        "0806",
        "0808",
        "0809",
        "0886",
        "0888",
        "0889",
        "0906",
        "0908",
        "0909",
        "0986",
        "0988",
        "0989",
        "8606",
        "8608",
        "8609",
        "8686",
        "8688",
        "8689",
        "8806",
        "8808",
        "8809",
        "8886",
        "8888",
        "8889",
        "8906",
        "8908",
        "8909",
        "8986",
        "8988",
        "8989",
    }
