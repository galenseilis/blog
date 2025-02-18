// car.rs

use std::cmp::Ordering;
use std::collections::BinaryHeap;
use std::cmp::Reverse;

#[derive(Debug, PartialEq, PartialOrd)]
enum EventType {
    Parking,
    Driving,
}


#[derive(Debug, PartialEq, PartialOrd)]
struct Event {
    time: f64,
    event_type: EventType
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
}

impl Event {
    fn new(time: f64, event_type: EventType) -> Self {
        Self { time, event_type }
    }

    fn execute(&self, env: &mut Environment) {
        match self.event_type {
            EventType::Parking => {
                println!("Start parking at {}", self.time);
                let parking_duration = 5.0;
                env.schedule_event(Event::new(self.time + parking_duration, EventType::Driving));
            }
            EventType::Driving => {
                println!("Start driving at {}", self.time);
                let trip_duration = 2.0;
                env.schedule_event(Event::new(self.time + trip_duration, EventType::Parking));
            }
        }
    }
}


fn main(){
let mut env = Environment::new();

// Schedule the initial clock event
env.schedule_event(Event::new(0.0, EventType::Parking));

// Run the simulation until max time
env.run_until(15.0);
}
