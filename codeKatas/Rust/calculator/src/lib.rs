// The &'static here means the return type has a static lifetime.
// This is a Rust feature that you don't need to worry about now.

pub fn add(input: &str) -> i32 {
    if input == "" {
        return 0;
    }
    else {
        let mut delimeter = ',';
        if input.contains("//") {
            delimeter = input.replace("//", "").chars().next().unwrap();
        }

        let numbers = input.replace("\n", &delimeter.to_string());
        let list_of_numbers = numbers.split(",");
        let mut sum = 0;
        for number in list_of_numbers {
            let my_int: i32 = number.parse().unwrap();
            // catch!(error: ParseIntError {
            //     continue;
            // });
            sum = sum + my_int;
        }
        return sum;
    }
}
