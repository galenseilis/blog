use std::collections::{BinaryHeap, HashMap};
use std::cmp::Ordering;

struct Event {
    time: f64,
    action: Box<dyn FnMut(&mut EventScheduler) -> Option<String>>,
    context: HashMap<String, String>,
    active: bool,
    }

impl Clone for Event {
    fn clone(&self) -> Self {
        Event {
            time: self.time,
            action: Box::new(|_| None),
            context: self.context.clone(),
            active: self.active,
            }
        }
    }

impl Event {
    fn new(time: f64, action: Option<Box<dyn FnMut(&mut EventScheduler) -> Option<String>>>, context: Option<HashMap<String, String>>) -> Self {
        Event {
            time,
            action: action.unwrap_or_else(|| Box::new(|_| None)),
            context: context.unwrap_or_default(),
            active: true,
            }
    }

    fn run(&mut self, scheduler: &mut EventScheduler) -> Option<String> {
        if self.active {
           (self.action)(scheduler)
        } else {
            None
        }
    }
}

impl PartialEq for Event {
    fn eq(&self, other: &Self) -> bool {
        self.time == other.time
    }
}

impl Eq for Event {}

impl PartialOrd for Event {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl Ord for Event {
    fn cmp(&self, other: &Self) -> Ordering {
        other.time.partial_cmp(&self.time).unwrap()
    }
}

struct EventScheduler {
    current_time: f64,
    event_queue: BinaryHeap<Event>,
    event_log: Vec<(Event, Option<String>)>,
}

impl EventScheduler {
    fn new() -> Self {
        EventScheduler {
            current_time: 0.0,
            event_queue: BinaryHeap::new(),
            event_log: Vec::new(),
        }
    }

    fn schedule(&mut self, event: Event) {
        self.event_queue.push(event);
    }

    fn timeout(&mut self, delay: f64, action: Option<Box<dyn FnMut(&mut EventScheduler) -> Option<String>>>, context: Option<HashMap<String, String>>) {
        let event = Event::new(self.current_time + delay, action, context);
        self.schedule(event);
    }

    fn run(&mut self, stop: Box<dyn Fn(&Self) -> bool>, log_filter: Option<Box<dyn Fn(&Event, &Option<String>) -> bool>>)  -> Vec<(Event, Option<String>)> {
        let log_filter = log_filter.unwrap_or_else(|| Box::new(|_, _| true));
        while !stop(self) {
            if let Some(mut event) = self.event_queue.pop() {
                self.current_time = event.time;
                let event_result = event.run(self);
                if log_filter(&event, &event_result) {
                    self.event_log.push((event, event_result));
                }
            } else {
                break;
            }
        }
        self.event_log.clone()
    }

    fn run_until_max_time(&mut self, max_time: f64) -> Vec<(Event, Option<String>)> {
        self.run(Box::new(stop_at_max_time_factory(max_time)), None)
    }
}

fn stop_at_max_time_factory(max_time: f64) -> Box<dyn Fn(&EventScheduler) -> bool> {
    Box::new(move |scheduler: &EventScheduler| {
        scheduler.current_time >= max_time
        || scheduler.event_queue.peek().map_or(true, |event| event.time >= max_time)
    })
}


fn main() {
    let mut scheduler = EventScheduler::new();

    let action = Box::new(|scheduler: &mut EventScheduler| {
        println!("Event executed at time {}", scheduler.current_time);
        // Schedule another event
        scheduler.timeout(1.0, None, None);
        Some(String::from("Scheduled another event"))
    });

    scheduler.timeout(5.0, Some(action), None);

    let log = scheduler.run_until_max_time(10.0);

    for (event, result) in log.iter() {
        println!("Event at time {}: {:?}", event.time, result);
    }
}
