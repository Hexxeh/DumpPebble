#include <pebble.h>

#define DUMP_START 0x8000000
#define DUMP_END 0x80001F0
#define BLOCK_SIZE 32

int main(void) {
  const unsigned char* start_addr = (unsigned char*) DUMP_START;
  const unsigned char* end_addr = (unsigned char*) DUMP_END;
  const size_t buffer_len = 2 * BLOCK_SIZE + 1;
  const char *digit = "0123456789ABCDEF";

  unsigned char buffer[buffer_len];
  unsigned char* p;
  int step_bytes = BLOCK_SIZE;
  int bytes_left = 0;

  for(const unsigned char* current_addr = start_addr; current_addr < end_addr; current_addr += BLOCK_SIZE)
  {
    p = buffer;
    bytes_left = end_addr - current_addr;
    step_bytes = bytes_left < BLOCK_SIZE ? bytes_left : BLOCK_SIZE;
    for(int i = 0; i < step_bytes; i++)
    {
      const unsigned char current_byte = *(current_addr+i);
      *p++ = digit[current_byte >> 4];
      *p++ = digit[current_byte & 0x0F];
    }
    *p = '\0';
    APP_LOG(APP_LOG_LEVEL_DEBUG, "%p: %s", current_addr, buffer);
  }
}
