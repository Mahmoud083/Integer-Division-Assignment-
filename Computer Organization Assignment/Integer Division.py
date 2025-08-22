def integer_division(dividend, divisor, output_file=None):
    # Initializing the values for 64-bit
    n = 64
    quotient = 0
    remainder = dividend

    # We format for output
    output = []
    output.append(f"Iteration\tStep\t\tQuotient\tDivisor\t\tRemainder")

    # In here, we perform the algorithm for n+1 steps
    for i in range(n + 1):
        output.append(f"{i}\t\tInitial values\t{quotient:064b}\t{divisor:064b}\t{remainder:064b}")

        # Step 1: Remainder = Remainder - Divisor
        remainder -= divisor
        output.append(f"{i}\t\tRem = Rem - Div\t{quotient:064b}\t{divisor:064b}\t{remainder:064b}")

        # Step 2: If remainder < 0
        if remainder < 0:
            quotient = quotient << 1
            remainder += divisor  # Restore the original value of remainder
            output.append(f"{i}\t\tRestore Rem\t{quotient:064b}\t{divisor:064b}\t{remainder:064b}")
        else:
            quotient = (quotient << 1) | 1
            output.append(f"{i}\t\tRem >= 0\t{quotient:064b}\t{divisor:064b}\t{remainder:064b}")

        # Step 3: Shift Divisor right
        divisor >>= 1
        output.append(f"{i}\t\tShift Div right\t{quotient:064b}\t{divisor:064b}\t{remainder:064b}")

    # Print or write the result
    result = "\n".join(output)
    if output_file:
        with open(output_file, "w") as file:
            file.write(result)
    else:
        print(result)

# Example usage for 64 bit
dividend = 0b0000011100000000000000000000000000000000000000000000000000000111
divisor = 0b0000001000000000000000000000000000000000000000000000000000000010
integer_division(dividend, divisor, output_file="output.txt")
