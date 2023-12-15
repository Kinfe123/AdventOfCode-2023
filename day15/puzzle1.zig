const std = @import("std");
const Allocator = std.mem.Allocator;
const List = std.ArrayList;
const Map = std.AutoHashMap;
const StrMap = std.StringHashMap;
const BitSet = std.DynamicBitSet;

const util = @import("utils.zig");
const gpa = util.gpa;

const data = @embedFile("./test.txt");
var temp: []u8 = null;

// fn getTypeInfo(any: anytype) std.TypeInfo {
//     return @typeInfo(any);
// }
// fn hash(curr: []const u8) u32 {
//     var summ: u32 = 0;
//     for (curr) |i| {
//         summ += @as(u32, i);
//         summ *= 17;
//         summ %= 256;
//     }
//     return summ;
// }
pub fn main() !void {
    // const allocator = std.heap.page_allocator;
    var each = std.mem.split(u8, data, ",");
    var summ: u32 = 0;
    while (each.next()) |word| {
        for (word) |i| {
            print({} , .{i});
            summ += @as(u32, i);
            summ *= 17;
            summ %= 256;
        }
    }
    print("{}" , .{summ});

  
}

// Useful stdlib functions
const tokenizeAny = std.mem.tokenizeAny;
const tokenizeSeq = std.mem.tokenizeSequence;
const tokenizeSca = std.mem.tokenizeScalar;
const splitAny = std.mem.splitAny;
const splitSeq = std.mem.splitSequence;
const splitSca = std.mem.splitScalar;
const indexOf = std.mem.indexOfScalar;
const indexOfAny = std.mem.indexOfAny;
const indexOfStr = std.mem.indexOfPosLinear;
const lastIndexOf = std.mem.lastIndexOfScalar;
const lastIndexOfAny = std.mem.lastIndexOfAny;
const lastIndexOfStr = std.mem.lastIndexOfLinear;
const trim = std.mem.trim;
const sliceMin = std.mem.min;
const sliceMax = std.mem.max;

const parseInt = std.fmt.parseInt;
const parseFloat = std.fmt.parseFloat;

const print = std.debug.print;
const assert = std.debug.assert;

const sort = std.sort.block;
const asc = std.sort.asc;
const desc = std.sort.desc;
