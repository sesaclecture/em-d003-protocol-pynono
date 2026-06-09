# 문제 1.
# GPIO 입력 레벨을 상태 문자열로 변환하세요.
def gpio_level_to_state(level):
    if level == 0:
        return "LOW"
    elif level == 1:
        return "HIGH"
    else:
        return "UNKNOWN"


# 문제 2.
# UART 송신용 패킷을 생성하세요.
def make_uart_tx_packet(message):

    return (message + "\n").encode()


# 문제 3.
# UART 수신 패킷을 파싱하세요.
def parse_uart_rx_packet(packet):
    return packet.decode().rstrip('\n')


# 문제 4.
# I2C 7-bit 주소가 유효한지 확인하세요.
def is_valid_i2c_address(address):
    return 0 <= address <= 0x7F


# 문제 5.
# SPI 전송 프레임을 생성하세요.
def make_spi_transfer_frame(command, payload):
    return [command, len(payload)] + payload
