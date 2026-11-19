pub fn get_gstreamer_mic(preferred: Option<&str>) -> anyhow::Result<(String, String)> {
    let monitor = gst::DeviceMonitor::new();
    monitor.add_filter(Some("Audio/Source"), None);
    monitor.start()?;

    let devices = monitor.devices();
    monitor.stop();

    let mut best_device = None;
    let mut highest_score = -1;

    println!("Probing audio devices for input:");
    for device in devices {
        println!("    Found device: {}", device.display_name());

        let props = device.properties();
        let bus = props
            .as_ref()
            .and_then(|p| p.get::<&str>("device.bus").ok())
            .unwrap_or("");
        let device_class = props
            .as_ref()
            .and_then(|p| p.get::<&str>("device.class").ok())
            .unwrap_or("");
        let device_id = props
            .as_ref()
            .and_then(|p| p.get::<&str>("node.name").ok())
            .unwrap_or("");

        let device_name = device.display_name().to_string();
        let is_monitor =
            device_class == "monitor" || device_name.to_lowercase().contains("monitor");

        // Fallback ladder
        let score = if preferred == Some(device_id) {
            99
        } else if is_monitor {
            0
        } else if bus == "usb" || bus == "bluetooth" {
            50
        } else if bus == "pci" {
            30
        } else {
            10
        };

        if score > highest_score {
            highest_score = score;
            best_device = Some((device_name, String::from(device_id), is_monitor));
        }
    }

    if let Some((name, id, is_monitor)) = best_device {
        if is_monitor {
            eprintln!("WARNING: No hardware mic found. Falling back to monitor (echo risk)");
        }

        println!("Using microphone: {} ({})", name, id);
        Ok((name, id))
    } else {
        anyhow::bail!("No microphone found.");
    }
}
