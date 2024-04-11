


from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    silver_taxi = SilverServiceTaxi("Hummer", 100, 2)
    silver_taxi.drive(18)
    print(silver_taxi)
    print(silver_taxi.get_fare())

main()