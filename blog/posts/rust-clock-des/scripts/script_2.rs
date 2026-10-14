#[derive(Debug, PartialEq, PartialOrd)]
struct Event {
    time: f64,
}

impl Eq for Event {}

impl Ord for Event {
    fn cmp(&self, other: &Self) -> Ordering {
        self.partial_cmp(other).unwrap_or(Ordering::Equal)
    }
}

impl Event {
    fn new(time: f64) -> Self {
        Self { time }
    }

    fn execute(&self, env: &mut Environment) {
        println!("Clock event executed at time: {}", self.time);
        env.schedule_event(Event::new(self.time + 0.5)); // Reschedule the clock event
    }
}
