def is_board_valid(board):
        return len( list( filter(lambda x: ( (x == 0) or (x == 1) or (x == 2) ) , board) ) ) == len(board)

def format_board_dat(board_intrey):
    return tuple( [ int(y) for y in board_intrey.rstrip().lstrip().split(" ") ] )

def get_board_dat(path):
    dat = open(path).readlines()
    board_dat = {}

    dat_index = 0
    while dat_index < len(dat):
        board_dat[ format_board_dat( dat[dat_index] ) ] = format_board_dat( dat[dat_index + 1] )
        dat_index += 2

    return board_dat

def emoji_board(board: str):

    board = list(board.strip(" "))

    for x in range(len(board)):
        if (x == 5) or (x == 13):
            board.insert(x, "\n")
    
    board = "".join(board)

    out = board.replace("0", ":white_large_square:").replace("1", ":negative_squared_cross_mark:").replace("2", ":o2:")
    return "\n" + out

def from_emoji_board(board: str):
    converted = board.replace("⬜", "0").replace("❎", "1").replace("🅾", "2").strip("\n").strip(" ")
    out = [str(char) for char in converted if char in "012"]
    return tuple(out)
