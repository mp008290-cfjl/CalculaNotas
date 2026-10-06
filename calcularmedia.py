def calcula_media_aritmetica(nota_1, nota_2, nota_3):
    return ((nota_1 * 2) + (nota_2 * 3) + (nota_3 * 5)) / 10


print("programa para calcular a média de duas notas")

nota_1 = float(input("por favor,diga a primeira nota: "))
nota_2 = float(input("por favor,diga a segunda nota: "))
nota_3 = float(input("por favor,diga a terceira nota: "))

media_ponderada = calcula_media_aritmetica(nota_1, nota_2, nota_3)


print(f"a média final é {media_ponderada:.2f}")

