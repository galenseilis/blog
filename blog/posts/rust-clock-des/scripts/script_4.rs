fn main() {
    let mut env = Environment::new();

    // Schedule the initial clock event
    env.schedule_event(Event::new(0.0));

impl Event {
    fn new(time: f64) -> Self {
        Self { time }
    }

    fn execute(&self, env: &mut Environment) {
        println!("Clock event executed at time: {}", self.time);
        env.schedule_event(Event::new(self.time + 0.5)); // Reschedule the clock event
    }
}
    // Run the simulation until max time
    env.run_until(5.0);

    // Print the current time after simulation
    println!("Simulation ended at time: {}", env.now());
}
