def httpcodes(request):
    match request:
        case 100:
            print(100)

        case 200:
            print(200)

        case 300:
            print(300)

        case 400:
            print(400)

        case 330 | 450 | 500:

            return 'Not allowed'

        case __:
            print('Unknown error')

httpcodes(400)