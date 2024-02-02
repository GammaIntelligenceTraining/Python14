# 7 *Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
#     Примеры:
#     1234565 seconds = 14d 6:56:5

seconds = 1234565

days = seconds // (24 * 60 * 60)
seconds %= 24 * 60 * 60
hours = seconds // (60 * 60)
seconds %= 60 * 60
minutes = seconds // 60
seconds %= 60

print(f'{days}d {hours}:{minutes}:{seconds}')