// clock.rs

use std::cmp::Ordering;
use std::collections::BinaryHeap;
use std::cmp::Reverse;

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

struct Environment {
    event_queue: BinaryHeap<Reverse<Event>>,
    clock: f64,
}

impl Environment {
    fn new() -> Self {
        Self {
            event_queue: BinaryHeap::new(),
            clock: 0.0,
        }
    }

    fn schedule_event(&mut self, event: Event) {
        self.event_queue.push(Reverse(event));
    }

    fn run_until(&mut self, end_time: f64) {
        while let Some(Reverse(current_event)) = self.event_queue.pop() {
            if current_event.time < end_time {
                self.clock = current_event.time;
                current_event.execute(self);
            } else {
                self.clock = end_time;
                break;
            }
        }
    }

    fn now(&self) -> f64 {
        self.clock
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

fn main() {
    let mut env = Environment::new();

    // Schedule the initial clock event
    env.schedule_event(Event::new(0.0));

    // Run the simulation until max time
    env.run_until(5.0);

    // Print the current time after simulation
    println!("Simulation ended at time: {}", env.now());
}
