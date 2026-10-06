import funcao_mediaponderada


print("programa para calcular a média de duas notas")

nota_1 = float(input("por favor,diga a primeira nota: "))
nota_2 = float(input("por favor,diga a segunda nota: "))
nota_3 = float(input("por favor,diga a terceira nota: "))

media_ponderada = funcao_mediaponderada.calcula_media_aritmetica(nota_1, nota_2, nota_3)


print(f"a média final é {media_ponderada:.2f}")

