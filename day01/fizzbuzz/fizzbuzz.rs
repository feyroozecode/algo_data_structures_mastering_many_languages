fn main() {
    fizzBuzzer();
}

fn fizzBuzzer() /*-> String*/
{
    let mut responses: [&str; 2] = ["Fizz", "Buzz"];

    for i in 0..100 {
        let mut output = String::new();

        if i % 3 == 0 && i % 5 == 0 {
            output = responses[0].to_string() + &responses[1].to_string();

            println!("{}", output);
        } else if i % 3 == 0 {
            output = responses[0].to_string();
            println!("{}", output);
        } else if i % 5 == 0 {
            output = responses[1].to_string();

            println!("{}", output);
        }

        output = i.to_string();

        println!("{}", output);
    }
}
