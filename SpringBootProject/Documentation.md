# Spring Boot Project Documentation

## Table of Contents

1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [Components](#components)
    - [SpringBootProjectApplication](#springbootprojectapplication)
    - [Device Entity](#device-entity)
    - [DeviceRepository](#devicerepository)
    - [DeviceService](#deviceservice)
    - [DeviceController](#devicecontroller)
    - [RestTemplateConfig](#resttemplateconfig)
4. [Configuration](#configuration)
5. [Usage](#usage)
    - [Running the Application](#running-the-application)
    - [API Endpoints](#api-endpoints)
6. [Deployment](#deployment)
7. [Conclusion](#conclusion)

---

## 1. Introduction <a name="introduction"></a>

This documentation provides an overview of the **Spring Boot Project**, detailing its structure, components, configurations, and usage. The project aims to manage devices using a RESTful API and integrates with a Python-based service for price prediction.

## 2. Project Structure <a name="project-structure"></a>

The project follows a typical Spring Boot structure with the following main components:

- `.idea/`: IntelliJ IDEA project configuration folder (IDE-specific).
- `src/`: Source folder containing Java source code.
  - `main/`: Main application code.
    - `java/`: Java packages.
      - `com.example.springbootproject/`: Main package.
        - `SpringBootProjectApplication.java`: Spring Boot application entry point.
        - `config/`: Configuration classes.
          - `RestTemplateConfig.java`: Configuration for `RestTemplate`.
        - `controller/`: REST controllers.
          - `DeviceController.java`: Controller handling device endpoints.
        - `entity/`: JPA entities.
          - `Device.java`: Entity class representing a device.
        - `repository/`: Spring Data repositories.
          - `DeviceRepository.java`: Repository interface for `Device` entities.
        - `service/`: Service classes.
          - `DeviceService.java`: Service class for device-related operations.
  - `test/`: Folder for test code (not detailed in this documentation).

- `data/`: Folder containing CSV files used for data operations.
- `notebooks/`: Folder containing Jupyter notebooks for data analysis and model training.
- `saved_model/`: Folder for storing trained machine learning models.

## 3. Components <a name="components"></a>

### 3.1 SpringBootProjectApplication <a name="springbootprojectapplication"></a>

- **Description**: Main entry point of the Spring Boot application.
- **File**: `SpringBootProjectApplication.java`

```java
package com.example.springbootproject;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;

@SpringBootApplication
@EnableJpaRepositories(basePackages = "com.example.springbootproject.repository")
public class SpringBootProjectApplication {

    public static void main(String[] args) {
        SpringApplication.run(SpringBootProjectApplication.class, args);
    }
}
```

### 3.2 Device Entity <a name="device-entity"></a>

- **Description**: Represents a device entity stored in the database.
- **File**: `Device.java`

```java
package com.example.springbootproject.entity;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import lombok.Data;

@Data
@Entity
public class Device {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private int batteryPower;
    private boolean blue;
    private double clockSpeed;
    // Other fields omitted for brevity
    private int priceRange;
}
```

### 3.3 DeviceRepository <a name="devicerepository"></a>

- **Description**: Interface for performing CRUD operations on `Device` entities.
- **File**: `DeviceRepository.java`

```java
package com.example.springbootproject.repository;

import com.example.springbootproject.entity.Device;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface DeviceRepository extends JpaRepository<Device, Long> {
}
```

### 3.4 DeviceService <a name="deviceservice"></a>

- **Description**: Service class for managing device operations, including CRUD and price prediction.
- **File**: `DeviceService.java`

```java
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

    // Methods for managing devices (getAllDevices, getDeviceById, addDevice, updateDevicePriceRange, predictDevicePrice)
    // Implementation provided earlier in the conversation

}
```

### 3.5 DeviceController <a name="devicecontroller"></a>

- **Description**: REST controller for handling HTTP requests related to devices.
- **File**: `DeviceController.java`

```java
package com.example.springbootproject.controller;

import com.example.springbootproject.entity.Device;
import com.example.springbootproject.service.DeviceService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/devices")
public class DeviceController {

    @Autowired
    private DeviceService deviceService;

    // REST endpoints for managing devices (getAllDevices, getDeviceById, addDevice, predictDevicePrice)
    // Implementation provided earlier in the conversation

}
```

### 3.6 RestTemplateConfig <a name="resttemplateconfig"></a>

- **Description**: Configuration class for `RestTemplate`.
- **File**: `RestTemplateConfig.java`

```java
package com.example.springbootproject.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.client.RestTemplate;

@Configuration
public class RestTemplateConfig {

    @Bean
    public RestTemplate restTemplate() {
        return new RestTemplate();
    }
}
```

## 4. Configuration <a name="configuration"></a>

- **Application Configuration**: `application.properties`
  - Location: `src/main/resources/application.properties`
  
  ```properties
  spring.application.name=SpringBootProject
  spring.datasource.url=jdbc:postgresql://localhost:5432/devicesdb
  spring.datasource.username=postgres
  spring.datasource.password=3969
  spring.jpa.hibernate.ddl-auto=update
  spring.jpa.show-sql=true
  spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.PostgreSQLDialect
  ```

## 5. Usage <a name="usage"></a>

### 5.1 Running the Application <a name="running-the-application"></a>

1. Ensure PostgreSQL is running with the correct database (`devicesdb`).
2. Run the `SpringBootProjectApplication` class as a Java application.
3. Access the application at `http://localhost:8080`.

### 5.2 API Endpoints <a name="api-endpoints"></a>

- **Get All Devices**: `GET /api/devices`
  - Retrieves all devices stored in the database.

- **Get Device by ID**: `GET /api/devices/{id}`
  - Retrieves a specific device by its ID.

- **Add Device**: `POST /api/devices`
  - Adds a new device to the database.

- **Predict Device Price**: `POST /api/devices/predict/{deviceId}`
  - Predicts the price range for a device using a Python-based service and updates the device in the database.

## 6. Deployment <a name="deployment"></a>

- **Deployment Instructions**: Deploy the application to a production environment using Docker, Kubernetes, or any other preferred method. Ensure database configuration (`application.properties`) is correctly set for the production environment.

