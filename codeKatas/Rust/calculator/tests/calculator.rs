use calculator;

#[test]
fn test_add_returns_0_if_empty_string() {
    assert_eq!(0, calculator::add(""));
}

#[test]
fn test_add_returns_number_only_one_number() {
    assert_eq!(2, calculator::add("2"));
}

#[test]
fn test_add_returns_sum_of_2_numbers() {
    assert_eq!(3, calculator::add("1,2"))
}

#[test]
fn test_add_returns_sum_of_5_numbers() {
    assert_eq!(15, calculator::add("1,2,3,4,5"))
}

#[test]
fn test_add_returns_sum_with_new_lines_between_numbers() {
    assert_eq!(6, calculator::add("1\n2,3"))
}   

// #[test]
// fn test_add_allows_setting_of_delimeter() {
//     assert_eq!(6, calculator::add("//;1\n2;3"))
// }   