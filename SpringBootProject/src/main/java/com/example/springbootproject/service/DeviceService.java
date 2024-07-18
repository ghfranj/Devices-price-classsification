package com.example.springbootproject.service;

import com.example.springbootproject.entity.Device;
import com.example.springbootproject.repository.DeviceRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.List;
import java.util.Optional;

@Service
public class DeviceService {

    @Autowired
    private DeviceRepository deviceRepository;

    @Autowired
    private RestTemplate restTemplate;

    private static final String PYTHON_API_URL = "http://localhost:5000/predict";

    public List<Device> getAllDevices() {
        return deviceRepository.findAll();
    }

    public Optional<Device> getDeviceById(Long id) {
        return deviceRepository.findById(id);
    }

    public Device addDevice(Device device) {
        return deviceRepository.save(device);
    }

    public Device updateDevicePriceRange(Long id, int priceRange) {
        Device device = deviceRepository.findById(id).orElseThrow(() -> new RuntimeException("Device not found"));
        device.setPriceRange(priceRange);
        return deviceRepository.save(device);
    }

    public int predictDevicePrice(Device device) {
        // Call the Python service to predict the price
        int predictedPriceRange = restTemplate.postForObject(PYTHON_API_URL, device, Integer.class);
        return predictedPriceRange;
    }
}
